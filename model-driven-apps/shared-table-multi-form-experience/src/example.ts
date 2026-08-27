/**
 * Shared-Table Multi-Form Experience
 *
 * Sanitized illustrative pattern.
 * Reusable Shared-Table Multi-Form Experience engineering pattern.
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
  console.debug('Shared-Table Multi-Form Experience', { id, status });
}
