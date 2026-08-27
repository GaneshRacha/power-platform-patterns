// Citizen vs Worker Experience Separation
// Reusable Citizen vs Worker Experience Separation engineering pattern.
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
