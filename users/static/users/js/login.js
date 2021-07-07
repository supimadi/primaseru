(() => {
  'use strict';
  window.addEventListener('load', () => {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = $('.login-form');
    let loginButton = $('.login-button');
    // Loop over them and prevent submission
    let validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', (e) => {
        if (form.checkValidity() === false) {
          e.preventDefault();
          e.stopPropagation();
        }
          loginButton.prop('disabled', true);
          loginButton.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Loading...</span>');
      }, false);
    });
  }, false);
})();
