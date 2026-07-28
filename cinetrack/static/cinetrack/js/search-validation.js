document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#search-query-form');
  const input = form?.querySelector('#search-query');
  const error = form?.querySelector('#search-query-error');

  if (!form || !input || !error) return;

  const hideError = () => {
    error.hidden = true;
    input.classList.remove('is-invalid');
    input.removeAttribute('aria-invalid');
  };

  const showError = () => {
    error.hidden = false;
    input.classList.add('is-invalid');
    input.setAttribute('aria-invalid', 'true');
    input.focus();
  };

  form.addEventListener('submit', (event) => {
    if (input.value.trim()) {
      hideError();
      return;
    }

    event.preventDefault();
    showError();
  });

  input.addEventListener('input', () => {
    if (input.value.trim()) {
      hideError();
    }
  });
});
