using Microsoft.Xrm.Sdk;
using System.Text.Json;

namespace Demo.PowerPlatform.Plugins;

public sealed class ParentChildCalculationPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        if (context.Stage != 20 || context.MessageName != "Update" ||
            !context.InputParameters.TryGetValue("Target", out var value) || value is not Entity target ||
            target.LogicalName != "demo_request" || !target.Contains("demo_childpayload"))
            return;

        var payload = target.GetAttributeValue<string>("demo_childpayload");
        if (string.IsNullOrWhiteSpace(payload))
        {
            target["demo_totalamount"] = 0m;
            return;
        }

        ChildLine[] lines;
        try
        {
            lines = JsonSerializer.Deserialize<ChildLine[]>(payload) ?? Array.Empty<ChildLine>();
        }
        catch (JsonException)
        {
            throw new InvalidPluginExecutionException("Child data is not valid JSON.");
        }

        var total = lines.Sum(line => Math.Max(0, line.Quantity) * Math.Max(0m, line.UnitAmount));
        target["demo_totalamount"] = total;
    }

    private sealed record ChildLine(int Quantity, decimal UnitAmount);
}
