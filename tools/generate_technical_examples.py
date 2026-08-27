from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', '.github', 'tools'}
CODE_EXTENSIONS = {'.ts', '.tsx', '.js', '.cs', '.json', '.xml', '.sql', '.dax', '.ps1', '.yml', '.yaml', '.kql', '.fx'}


def slug_to_type(slug: str) -> str:
    return ''.join(part.capitalize() for part in re.split(r'[^a-zA-Z0-9]+', slug) if part) or 'Pattern'


def read_metadata(folder: Path) -> tuple[str, str, str]:
    text = (folder / 'README.md').read_text(encoding='utf-8') if (folder / 'README.md').exists() else ''
    title = re.search(r'^#\s+(.+)$', text, re.M)
    summary_match = re.search(r'## Summary\s+\n+(.+?)(?:\n\n##|\Z)', text, re.S)
    level_match = re.search(r'\*\*Level:\*\*\s*([^\n]+)', text)
    title_value = title.group(1).strip() if title else folder.name.replace('-', ' ').title()
    summary = re.sub(r'\s+', ' ', summary_match.group(1).strip()) if summary_match else f'Reusable {title_value} engineering pattern.'
    level = level_match.group(1).strip() if level_match else 'Core'
    return title_value, summary, level


def has_concrete_artifact(folder: Path) -> bool:
    for path in folder.rglob('*'):
        if path.is_file() and path.name != 'README.md' and path.suffix.lower() in CODE_EXTENSIONS:
            return True
    return False


def ensure(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + '\n', encoding='utf-8')
    return True


def ts_example(title: str, summary: str) -> tuple[str, str]:
    return 'src/example.ts', f'''/**
 * {title}
 *
 * Sanitized illustrative pattern.
 * {summary}
 */
export type PatternContext = {{
  formContext: Xrm.FormContext;
}};

export function executePattern(context: PatternContext): void {{
  const form = context.formContext;
  const id = form.data.entity.getId().replace(/[{{}}]/g, '').toLowerCase();
  if (!id) return;

  // Keep schema names centralized and replace these demo aliases in a real solution.
  const status = form.getAttribute<number>('demo_status')?.getValue();
  if (status == null) return;

  // Pattern-specific behavior belongs here. Keep handlers idempotent and null-safe.
  console.debug('{title}', {{ id, status }});
}}
'''


def pcf_example(title: str, summary: str) -> tuple[str, str]:
    return 'src/ControlSkeleton.ts', f'''/**
 * {title}
 * Sanitized PCF skeleton: {summary}
 */
export interface PatternInputs {{
  value?: string;
  disabled?: boolean;
}}

export class ControlSkeleton {{
  private notifyOutputChanged?: () => void;
  private currentValue = '';

  public init(notifyOutputChanged: () => void): void {{
    this.notifyOutputChanged = notifyOutputChanged;
  }}

  public update(inputs: PatternInputs): void {{
    this.currentValue = inputs.value ?? '';
    // Render from stable state; avoid Dataverse writes inside the render path.
  }}

  public setValue(value: string): void {{
    if (value === this.currentValue) return;
    this.currentValue = value;
    this.notifyOutputChanged?.();
  }}

  public getOutputs(): PatternInputs {{
    return {{ value: this.currentValue }};
  }}
}}
'''


def csharp_plugin(title: str, summary: str, slug: str) -> tuple[str, str]:
    type_name = slug_to_type(slug) + 'Plugin'
    return f'src/{type_name}.cs', f'''using Microsoft.Xrm.Sdk;

namespace Demo.PowerPlatform.Patterns;

/// <summary>
/// {title}
/// Sanitized illustrative implementation: {summary}
/// </summary>
public sealed class {type_name} : IPlugin
{{
    public void Execute(IServiceProvider serviceProvider)
    {{
        var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var trace = (ITracingService)serviceProvider.GetService(typeof(ITracingService));

        if (!context.InputParameters.TryGetValue("Target", out var value) || value is not Entity target)
            return;

        if (context.Depth > 1)
            return;

        trace.Trace("{title}: {{Message}}/{{Stage}} for {{Entity}}", context.MessageName, context.Stage, target.LogicalName);

        // Keep the plugin entry point thin. Delegate real business rules to a testable service class.
        // Use filtering attributes, minimal queries, images, and transactions deliberately.
    }}
}}
'''


def integration_example(title: str, summary: str, slug: str) -> tuple[str, str]:
    type_name = slug_to_type(slug) + 'Client'
    return f'src/{type_name}.cs', f'''using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace Demo.PowerPlatform.Integration;

/// <summary>{title} — {summary}</summary>
public sealed class {type_name}
{{
    private readonly HttpClient _client;
    public {type_name}(HttpClient client) => _client = client;

    public async Task<string> SendAsync(Uri endpoint, string token, object payload, CancellationToken cancellationToken)
    {{
        if (endpoint.Scheme != Uri.UriSchemeHttps)
            throw new InvalidOperationException("HTTPS is required.");

        using var request = new HttpRequestMessage(HttpMethod.Post, endpoint);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);
        request.Headers.Add("x-correlation-id", Guid.NewGuid().ToString("N"));
        request.Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        using var response = await _client.SendAsync(request, cancellationToken);
        var body = await response.Content.ReadAsStringAsync(cancellationToken);
        if (!response.IsSuccessStatusCode)
            throw new InvalidOperationException($"Integration failed with HTTP {{(int)response.StatusCode}}.");
        return body;
    }}
}}
'''


def flow_example(title: str, summary: str) -> tuple[str, str]:
    payload = {
        '$schema': 'https://example.invalid/power-automate-pattern.schema.json',
        'title': title,
        'description': summary,
        'pattern': {
            'trigger': {'type': 'Dataverse', 'table': 'demo_request'},
            'guards': ['recordId is not empty', 'List rows result length > 0'],
            'scopes': ['Try', 'Catch', 'Finally'],
            'idempotencyKey': 'demo_correlationkey',
            'notes': 'Illustrative structure only; importable flow definition intentionally omitted.'
        }
    }
    return 'definition.sample.json', json.dumps(payload, indent=2)


def schema_example(title: str, summary: str, category: str) -> tuple[str, str]:
    payload = {
        'pattern': title,
        'category': category,
        'summary': summary,
        'entities': [
            {'logicalName': 'demo_parent', 'purpose': 'transaction or configuration parent'},
            {'logicalName': 'demo_child', 'purpose': 'related detail/history/configuration'}
        ],
        'rules': [
            'Use explicit relationships and stable business keys.',
            'Preserve historical references when configuration changes.',
            'Keep environment-specific values outside source code.'
        ]
    }
    return 'config/example.json', json.dumps(payload, indent=2)


def security_example(title: str, summary: str) -> tuple[str, str]:
    payload = {
        'pattern': title,
        'summary': summary,
        'personas': {
            'worker': ['read-owned', 'write-owned'],
            'supervisor': ['read-team', 'write-team', 'assign-team'],
            'administrator': ['configuration-maintenance']
        },
        'recordBoundary': 'Owner team / business unit security; UI visibility is not a security boundary.',
        'testCases': ['single role', 'combined roles', 'direct share', 'team reassignment']
    }
    return 'config/security-model.json', json.dumps(payload, indent=2)


def alm_example(title: str, summary: str) -> tuple[str, str]:
    return 'example/validate.ps1', f'''# {title}
# Sanitized illustrative validation script.
# {summary}

$ErrorActionPreference = 'Stop'

function Assert-Value([bool]$Condition, [string]$Message) {{
    if (-not $Condition) {{ throw $Message }}
}}

Write-Host 'Running pre-deployment checks...'
Assert-Value (Test-Path './README.md') 'Pattern documentation is missing.'

# In a real pipeline, add solution unpack validation, dependency checks,
# environment variable verification, component version checks, and import smoke tests.
Write-Host 'Validation completed.'
'''


def devops_example(title: str, summary: str) -> tuple[str, str]:
    return 'example/azure-pipelines.yml', f'''# {title}
# {summary}
trigger:
  branches:
    include: [ main ]

stages:
- stage: Validate
  jobs:
  - job: StaticChecks
    steps:
    - checkout: self
    - script: echo "Validate source, solution dependencies, and version contracts"
      displayName: Validate engineering artifacts

- stage: Package
  dependsOn: Validate
  jobs:
  - job: PackageSolution
    steps:
    - script: echo "Package managed solution / component artifact"
      displayName: Package
'''


def sql_example(title: str, summary: str) -> tuple[str, str]:
    return 'example/reconciliation.sql', f'''-- {title}
-- {summary}
-- Sanitized reconciliation pattern.
WITH source_rows AS (
    SELECT business_key, source_value
    FROM demo_source
), target_rows AS (
    SELECT business_key, target_value
    FROM demo_target
)
SELECT
    COALESCE(s.business_key, t.business_key) AS business_key,
    s.source_value,
    t.target_value,
    CASE
        WHEN s.business_key IS NULL THEN 'TARGET_ONLY'
        WHEN t.business_key IS NULL THEN 'SOURCE_ONLY'
        WHEN s.source_value <> t.target_value THEN 'MISMATCH'
        ELSE 'MATCH'
    END AS reconciliation_status
FROM source_rows s
FULL OUTER JOIN target_rows t ON t.business_key = s.business_key;
'''


def powerfx_example(title: str, summary: str) -> tuple[str, str]:
    return 'example/PowerFx.txt', f'''// {title}
// {summary}
// Sanitized Canvas App example.
With(
    {{ currentId: Coalesce(varSelectedId, GUID()) }},
    If(
        IsBlank(currentId),
        Notify("A record is required.", NotificationType.Error),
        Set(varIsBusy, true);
        // Perform guarded Patch/Collect/navigation logic here.
        Set(varIsBusy, false)
    )
)
'''


def dax_example(title: str, summary: str) -> tuple[str, str]:
    return 'example/measures.dax', f'''-- {title}
-- {summary}
Total Records := COUNTROWS('Fact')

Successful Records :=
CALCULATE(
    [Total Records],
    'Fact'[Outcome] = "Success"
)

Success Rate := DIVIDE([Successful Records], [Total Records], 0)
'''


def powerpages_example(title: str, summary: str) -> tuple[str, str]:
    return 'src/validation.js', f'''// {title}
// {summary}
(function () {{
  'use strict';

  function validate() {{
    const value = document.querySelector('[data-demo-field]')?.value?.trim();
    if (!value) {{
      return {{ valid: false, message: 'A value is required.' }};
    }}
    return {{ valid: true }};
  }}

  window.demoPatternValidation = validate;
}})();
'''


def production_example(title: str, summary: str) -> tuple[str, str]:
    return 'example/diagnostic.kql', f'''// {title}
// {summary}
// Illustrative operational query; adapt table names to the monitoring platform.
DemoOperations
| where TimeGenerated > ago(24h)
| summarize
    Requests = count(),
    Failures = countif(Result == "Failure"),
    P95DurationMs = percentile(DurationMs, 95)
  by Component
| extend FailureRate = todouble(Failures) / Requests
| order by FailureRate desc
'''


def example_for(category: str, title: str, summary: str, slug: str) -> tuple[str, str]:
    if category in {'javascript', 'model-driven-apps'}:
        return ts_example(title, summary)
    if category == 'pcf':
        return pcf_example(title, summary)
    if category == 'plugins':
        return csharp_plugin(title, summary, slug)
    if category == 'custom-api':
        return csharp_plugin(title, summary, slug)
    if category == 'integration':
        return integration_example(title, summary, slug)
    if category == 'power-automate':
        return flow_example(title, summary)
    if category in {'dataverse', 'architecture'}:
        return schema_example(title, summary, category)
    if category == 'security':
        return security_example(title, summary)
    if category == 'alm':
        return alm_example(title, summary)
    if category == 'devops':
        return devops_example(title, summary)
    if category == 'data-engineering':
        return sql_example(title, summary)
    if category == 'canvas-apps':
        return powerfx_example(title, summary)
    if category == 'power-bi':
        return dax_example(title, summary)
    if category == 'power-pages':
        return powerpages_example(title, summary)
    if category == 'production-engineering':
        return production_example(title, summary)
    return schema_example(title, summary, category)


def main() -> None:
    created = 0
    skipped = 0
    for category_dir in sorted(path for path in ROOT.iterdir() if path.is_dir() and path.name not in SKIP):
        category = category_dir.name
        for pattern_dir in sorted(path for path in category_dir.iterdir() if path.is_dir()):
            if not (pattern_dir / 'README.md').exists():
                continue
            if has_concrete_artifact(pattern_dir):
                skipped += 1
                continue
            title, summary, _ = read_metadata(pattern_dir)
            relative, content = example_for(category, title, summary, pattern_dir.name)
            if ensure(pattern_dir / relative, content):
                created += 1
    print(f'Created {created} technical examples; preserved {skipped} existing source-backed patterns.')


if __name__ == '__main__':
    main()
