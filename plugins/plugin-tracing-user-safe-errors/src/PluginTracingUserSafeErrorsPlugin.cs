using Microsoft.Xrm.Sdk;

namespace Demo.PowerPlatform.Patterns;

/// <summary>
/// Plugin Tracing & User-Safe Error Pattern
/// Sanitized illustrative implementation: Reusable Plugin Tracing & User-Safe Error Pattern engineering pattern.
/// </summary>
public sealed class PluginTracingUserSafeErrorsPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var trace = (ITracingService)serviceProvider.GetService(typeof(ITracingService));

        if (!context.InputParameters.TryGetValue("Target", out var value) || value is not Entity target)
            return;

        if (context.Depth > 1)
            return;

        trace.Trace("Plugin Tracing & User-Safe Error Pattern: {Message}/{Stage} for {Entity}", context.MessageName, context.Stage, target.LogicalName);

        // Keep the plugin entry point thin. Delegate real business rules to a testable service class.
        // Use filtering attributes, minimal queries, images, and transactions deliberately.
    }
}
