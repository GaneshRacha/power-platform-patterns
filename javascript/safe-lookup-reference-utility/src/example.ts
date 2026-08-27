/**
 * Safe Lookup Reference Utility
 *
 * Sanitized illustrative pattern.
 * Reusable Safe Lookup Reference Utility engineering pattern.
 */
export type PatternContext = {
  formContext: Xrm.FormContext;
};

export function executePattern(context: PatternContext): void {
  const form = context.formContext;
  const id = form.data.entity.getId().replace(/[{}]/g, '').toLowerCase();
  if (!id) return;

  // Keep schema names centralized and replace these demo aliases in a real solution.
  const status = form.getAttribute<number>('demo_status')?.getValue();
  if (status == null) return;

  // Pattern-specific behavior belongs here. Keep handlers idempotent and null-safe.
  console.debug('Safe Lookup Reference Utility', { id, status });
}
