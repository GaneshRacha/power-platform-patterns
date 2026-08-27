// External + Internal Shared Dataverse Model
// Reusable External + Internal Shared Dataverse Model engineering pattern.
(function () {
  'use strict';

  function validate() {
    const value = document.querySelector('[data-demo-field]')?.value?.trim();
    if (!value) {
      return { valid: false, message: 'A value is required.' };
    }
    return { valid: true };
  }

  window.demoPatternValidation = validate;
})();
