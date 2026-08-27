# Test scenarios

1. Parent is empty: child lookup remains unfiltered and no exception is thrown.
2. Parent is selected: child lookup shows only related records.
3. Parent changes: existing child value is cleared.
4. No matching records: lookup opens with an empty result set.
5. Inactive records: excluded when the optional active column is configured.
6. Form variant without the control: handler exits safely.
