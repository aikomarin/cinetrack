document.addEventListener('DOMContentLoaded', () => {
  if (!window.flatpickr) return;

  document.querySelectorAll('.ct-date-input').forEach((input) => {
    window.flatpickr(input, {
      locale: 'es',
      dateFormat: 'Y-m-d',
      altInput: true,
      altFormat: 'd/m/Y',
      allowInput: false,
      disableMobile: true,
      altInputClass: 'form-control ct-date-input ct-date-input-visible'
    });
  });
});
