# Effective-Dated Configuration — Sample Schema

Use an explicit configuration table when business rules change over time but historical transactions must retain their original context.

## `demo_configurationperiod`

| Column | Type | Purpose |
| --- | --- | --- |
| `demo_name` | Text | Human-readable configuration label |
| `demo_parentid` | Lookup | Parent program/configuration scope |
| `demo_startdate` | Date Only | Inclusive effective start |
| `demo_enddate` | Date Only | Inclusive effective end |
| `demo_isactive` | Yes/No | Operational activation flag |
| `statecode` | System | Soft-delete / inactive lifecycle |

## Transaction snapshot

`demo_request.demo_configurationperiodatregistration` is a lookup captured once when the transaction is first registered. Later changes to the active period do not rewrite that lookup.

## Validation rules

1. `startdate <= enddate`.
2. No overlapping active ranges for the same parent scope unless explicitly supported.
3. At most one operationally active period for a scope when the business process requires single-active behavior.
4. Historical transactions keep their original lookup even after the configuration period is deactivated.
