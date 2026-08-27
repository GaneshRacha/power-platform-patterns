# Registration Notes

Recommended step for the sanitized example:

- Message: `Update`
- Primary table: `demo_request`
- Stage: PostOperation (synchronous when same-transaction consistency is required)
- Filtering attribute: `demo_regionid`
- Pre Image alias: `PreImage`
- Pre Image columns: `demo_customerid`, `demo_periodid`, `demo_regionid`, `demo_status`

Use the smallest image/query column set needed by the rule. A depth guard prevents the synchronization updates from re-entering the same behavior indefinitely.
