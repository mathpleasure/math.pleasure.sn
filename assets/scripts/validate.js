(function () {
  // Script For Validate Form
  var forms = document.querySelectorAll('.needs-validation');

  // Func Validate
  function Validate(event) {
    Array.prototype.slice.call(forms).forEach(function (form) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated')
    })
  }

  // Get Inputs And Forms
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener('submit', function (event) {
        Validate(event);
      })
    })

})()