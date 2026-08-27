# Cross-record synchronization test cases

- Update the governed field on an eligible active record and verify peer records with the same customer + period synchronize.
- Verify records outside the configured lifecycle statuses are unchanged.
- Verify the current record is excluded from peer updates.
- Verify an unchanged value does not create unnecessary writes.
- Verify depth > 1 exits safely to prevent recursion.
- Verify missing customer or period context results in a safe no-op.
- Verify a failed peer update rolls back with the originating synchronous transaction when registered synchronously.
