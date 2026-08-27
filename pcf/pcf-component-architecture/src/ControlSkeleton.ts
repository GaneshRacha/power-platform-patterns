/**
 * Maintainable PCF Component Architecture
 * Sanitized PCF skeleton: Refactoring pattern that separates PCF lifecycle code, React components, data services, models, constants, and reusable utilities.
 */
export interface PatternInputs {
  value?: string;
  disabled?: boolean;
}

export class ControlSkeleton {
  private notifyOutputChanged?: () => void;
  private currentValue = '';

  public init(notifyOutputChanged: () => void): void {
    this.notifyOutputChanged = notifyOutputChanged;
  }

  public update(inputs: PatternInputs): void {
    this.currentValue = inputs.value ?? '';
    // Render from stable state; avoid Dataverse writes inside the render path.
  }

  public setValue(value: string): void {
    if (value === this.currentValue) return;
    this.currentValue = value;
    this.notifyOutputChanged?.();
  }

  public getOutputs(): PatternInputs {
    return { value: this.currentValue };
  }
}
