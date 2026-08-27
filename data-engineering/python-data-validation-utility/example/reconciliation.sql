-- Python Data Validation Utility
-- Reusable Python Data Validation Utility engineering pattern.
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
