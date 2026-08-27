# Defensive Dataverse Record ID Handling

## Failure this prevents

Dataverse actions fail when `recordId` resolves to null/empty or when `first()` is evaluated against an empty `List rows` result.

## Recommended flow shape

```text
Trigger
  ↓
Validate trigger row ID
  ↓
List rows using a selective filter
  ↓
Condition: length(body('List_rows')?['value']) > 0
  ├─ Yes → Compose first row ID → record-specific action
  └─ No  → Terminate / log a controlled not-found outcome
```

## Safe expressions

```text
length(outputs('List_rows')?['body/value'])
```

Only inside the `Yes` branch:

```text
first(outputs('List_rows')?['body/value'])?['demo_requestid']
```

For a trigger identifier:

```text
empty(triggerOutputs()?['body/demo_requestid'])
```

## Production guidance

- Do not dereference `first()` before checking array length.
- Keep error handling in Scopes and use Configure run after for failed/timed-out branches.
- Prefer idempotent downstream updates so retries do not create duplicates.
- Include a correlation/reference value in operational logging.
