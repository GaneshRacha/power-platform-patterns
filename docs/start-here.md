# Start Here — 10-Minute Engineering Review

If you are reviewing this repository for a Power Platform engineering role, these are the best places to start.

## 1. Reusable component engineering

**Generic Record Selector PCF**  
[Open pattern →](../pcf/generic-record-selector-pcf/)

Shows:
- reusable PCF architecture
- explicit Dataverse junction persistence
- TypeScript models/services
- PCF manifest and package structure
- lifecycle and testing considerations

## 2. Server-side Dataverse engineering

**Cross-Record Synchronization Plugin**  
[Open pattern →](../plugins/cross-record-synchronization-plugin/)

Shows:
- C# plugin pipeline usage
- depth/recursion protection
- minimal related-record queries
- lifecycle/status eligibility rules
- server-authoritative consistency

## 3. Secure integration

**Secure Service Integration**  
[Open pattern →](../custom-api/secure-service-integration/)

Shows:
- Custom API / C# service boundary
- HTTPS and endpoint trust validation
- OAuth-oriented server-side integration
- controlled responses and failure handling

## 4. Data architecture

**Effective-Dated Configuration**  
[Open pattern →](../dataverse/effective-dated-configuration/)

Shows:
- point-in-time configuration
- overlap/single-active rules
- historical lookup preservation
- reporting-friendly design

## 5. Automation reliability

**Defensive Dataverse Record ID Handling**  
[Open pattern →](../power-automate/defensive-dataverse-recordid-flow/)

Shows:
- guarded `List rows`
- safe `first()` usage
- null record ID prevention
- error scopes and idempotency guidance

## 6. Security architecture

**Team-Based Data Security**  
[Open pattern →](../security/team-based-data-security/)

Shows:
- owner-team boundaries
- least-privilege roles
- role-combination testing
- separation of UI navigation from real Dataverse security

## 7. ALM / production troubleshooting

**Dataverse Solution Import Troubleshooting**  
[Open pattern →](../alm/solution-import-troubleshooting/)

Shows:
- dependency diagnosis
- schema/type mismatch analysis
- root-component and form/view recovery
- managed-solution release thinking

## Architecture overview

For the visual system view, see the [Power Platform Architecture Atlas](architecture-atlas.md).

## Full library

The complete repository contains **136 documented and example-backed patterns** across Power Apps, Dataverse, JavaScript/TypeScript, PCF, C# plugins, Custom APIs, Power Automate, Azure integration, Power BI, security, ALM, DevOps, and production engineering.

[Return to repository home →](../README.md)
