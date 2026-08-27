# Team-based security implementation checklist

1. Define personas and the minimum Create/Read/Write/Append/Append To/Assign privileges each needs.
2. Use owner teams for operational ownership when groups need a shared record boundary.
3. Ensure automation assigns or reassigns records consistently; do not depend on UI filtering for security.
4. Test users with individual roles and combined roles because Dataverse privileges are additive.
5. Validate direct sharing, business-unit scope, and team membership changes.
6. Confirm model-driven navigation visibility aligns with privileges without presenting it as the security boundary.
