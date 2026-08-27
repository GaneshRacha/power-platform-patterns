using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Query;

namespace Demo.PowerPlatform.Plugins;

/// <summary>
/// Sanitized example: when a governed field changes on one active request,
/// synchronize the same field to other eligible requests for the same
/// customer and program period.
/// </summary>
public sealed class CrossRecordSynchronizationPlugin : IPlugin
{
    private static readonly HashSet<int> EligibleStatuses = new() { 100000000, 100000001, 100000002 };

    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var factory = (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
        var service = factory.CreateOrganizationService(context.UserId);

        if (context.Depth > 1 || context.MessageName != "Update" ||
            !context.InputParameters.TryGetValue("Target", out var value) || value is not Entity target ||
            target.LogicalName != "demo_request" || !target.Contains("demo_regionid"))
        {
            return;
        }

        if (!context.PreEntityImages.TryGetValue("PreImage", out var preImage))
            throw new InvalidPluginExecutionException("PreImage is required.");

        var customer = preImage.GetAttributeValue<EntityReference>("demo_customerid");
        var period = preImage.GetAttributeValue<EntityReference>("demo_periodid");
        var newRegion = target.GetAttributeValue<EntityReference>("demo_regionid");

        if (customer is null || period is null)
            return;

        var query = new QueryExpression("demo_request")
        {
            ColumnSet = new ColumnSet("demo_status", "demo_regionid"),
            Criteria = new FilterExpression(LogicalOperator.And)
        };
        query.Criteria.AddCondition("demo_requestid", ConditionOperator.NotEqual, context.PrimaryEntityId);
        query.Criteria.AddCondition("demo_customerid", ConditionOperator.Equal, customer.Id);
        query.Criteria.AddCondition("demo_periodid", ConditionOperator.Equal, period.Id);
        query.Criteria.AddCondition("statecode", ConditionOperator.Equal, 0);

        foreach (var related in service.RetrieveMultiple(query).Entities)
        {
            var status = related.GetAttributeValue<OptionSetValue>("demo_status")?.Value;
            if (status is null || !EligibleStatuses.Contains(status.Value))
                continue;

            var existingRegion = related.GetAttributeValue<EntityReference>("demo_regionid");
            if (existingRegion?.Id == newRegion?.Id)
                continue;

            var update = new Entity("demo_request", related.Id)
            {
                ["demo_regionid"] = newRegion
            };
            service.Update(update);
        }
    }
}
