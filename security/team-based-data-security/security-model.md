# Team-Based Dataverse Security Model

## Goal

Allow multiple operational groups to use shared Dataverse tables while preventing automatic cross-team access to records.

## Recommended model

```text
Business Unit
  ├─ Owner Team A → owns Team A records
  ├─ Owner Team B → owns Team B records
  └─ Shared reference/configuration tables → organization-readable as appropriate
```

## Role design

| Capability | Transaction table | Reference table | Configuration table |
| --- | --- | --- | --- |
| Read | User / Team scope | Org scope | Org or BU scope |
| Create | User / Team scope | Restricted | Restricted |
| Write | Owned records | Restricted | Admin/configurator only |
| Assign | Limited | N/A | Limited |
| Share | Avoid unless required | N/A | Avoid unless required |

## Rules

- Treat form visibility and sitemap hiding as UX only; they are not security boundaries.
- Assign records to owner teams consistently through server-side logic or controlled automation.
- Test combined-role behavior because effective privileges are additive.
- Avoid broad direct sharing when team ownership can model the access requirement cleanly.
