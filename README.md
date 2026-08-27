# Power Platform Engineering Patterns

A public-safe library of **136 reusable engineering patterns** across Microsoft Power Platform, Dataverse, PCF, C# plugins, Custom APIs, Power Automate, Azure integration, analytics, ALM, security, and production engineering.

Live portfolio: https://power-platform-portfolio-olive.vercel.app/

## Flagship source implementations

These patterns include real sanitized source/configuration in addition to documentation:

- [Generic Record Selector PCF](pcf/generic-record-selector-pcf/) — TypeScript models, Dataverse repository layer, architecture, and testing guidance
- [Dynamic Dataverse Lookup Filtering](javascript/dynamic-lookup-filtering/) — reusable Model-Driven App lookup filtering source
- [Status-Based Field Locking](javascript/status-based-field-locking/) — configurable lifecycle-driven UI locking helper
- [Secure Service Integration](custom-api/secure-service-integration/) — C# HTTPS/allowlist service gateway and Custom API contract
- [Dataverse Solution Import Troubleshooting](alm/solution-import-troubleshooting/) — structured ALM diagnosis and recovery playbook

## Why this repository exists

The portfolio website explains the work visually. This repository provides the technical evidence behind it: source examples, configuration patterns, architecture decisions, validation scenarios, and production considerations.

The patterns are intentionally generic. Organization-specific schema names, tenant URLs, credentials, client data, proprietary solution exports, and internal source code are excluded.

## Library

- [ALM](alm/)
- [Architecture](architecture/)
- [Canvas Apps](canvas-apps/)
- [Custom API](custom-api/)
- [Data Engineering](data-engineering/)
- [Dataverse](dataverse/)
- [DevOps](devops/)
- [Integration](integration/)
- [JavaScript](javascript/)
- [Model-Driven Apps](model-driven-apps/)
- [PCF](pcf/)
- [Plugins](plugins/)
- [Power Automate](power-automate/)
- [Power BI](power-bi/)
- [Power Pages](power-pages/)
- [Production Engineering](production-engineering/)
- [Security](security/)

## Repository approach

Not every one of the 136 patterns needs a fake standalone app. Each implementation is documented, and the highest-value patterns are progressively upgraded with meaningful sanitized source files, configuration, architecture, and tests.

## Public-safety boundary

See [SANITIZATION.md](SANITIZATION.md). Public examples use generic aliases and omit credentials, tenant URLs, production identifiers, proprietary solution exports, internal documentation, and organization-specific business terminology.

## Related repository

Website source: https://github.com/GaneshRacha/power-platform-portfolio
