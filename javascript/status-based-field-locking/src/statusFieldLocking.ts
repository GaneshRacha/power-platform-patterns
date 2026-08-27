type FormContext = any;

export interface LockingRule {
  lockedStatuses: number[];
  controls: string[];
}

export function applyStatusFieldLocking(
  formContext: FormContext,
  statusColumn: string,
  rule: LockingRule
): void {
  const statusAttribute = formContext.getAttribute(statusColumn);
  if (!statusAttribute) return;

  const status = statusAttribute.getValue();
  const shouldLock = rule.lockedStatuses.includes(status);

  for (const controlName of rule.controls) {
    const control = formContext.getControl(controlName);
    if (control?.setDisabled) control.setDisabled(shouldLock);
  }
}

export function registerStatusFieldLocking(
  formContext: FormContext,
  statusColumn: string,
  rule: LockingRule
): void {
  const apply = () => applyStatusFieldLocking(formContext, statusColumn, rule);
  formContext.getAttribute(statusColumn)?.addOnChange(apply);
  apply();
}
