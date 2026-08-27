/**
 * PCF Exclusive Option Selection Pattern
 * Sanitized PCF skeleton: Selection-control behavior where one configurable option is mutually exclusive with all other choices while existing data remains protected.
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
