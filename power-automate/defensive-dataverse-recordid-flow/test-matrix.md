# Flow validation matrix

| Scenario | Expected result |
| --- | --- |
| Trigger contains a valid row ID | Continue to selective Dataverse query |
| Trigger row ID is empty | Controlled terminate/log branch; no record action |
| List rows returns zero records | Do not evaluate `first()`; log not-found outcome |
| List rows returns one record | Compose the ID and continue |
| Downstream action times out | Catch scope captures failure and correlation value |
| Flow retries | Idempotent key prevents duplicate side effects |
