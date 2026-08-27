using Microsoft.Xrm.Sdk;

namespace Demo.PowerPlatform.Patterns;

/// <summary>
/// Custom API Input & Output Parameter Design
/// Sanitized illustrative implementation: Reusable Custom API Input & Output Parameter Design engineering pattern.
/// </summary>
public sealed class CustomApiInputOutputDesignPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var trace = (ITracingService)serviceProvider.GetService(typeof(ITracingService));

        if (!context.InputParameters.TryGetValue("Target", out var value) || value is not Entity target)
            return;

        if (context.Depth > 1)
            return;

        trace.Trace("Custom API Input & Output Parameter Design: {Message}/{Stage} for {Entity}", context.MessageName, context.Stage, target.LogicalName);

        // Keep the plugin entry point thin. Delegate real business rules to a testable service class.
        // Use filtering attributes, minimal queries, images, and transactions deliberately.
    }
}
