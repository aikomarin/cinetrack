document.addEventListener('DOMContentLoaded', () => {
  if (window.flatpickr) {
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
  }

  const syncCustomSelect = (select) => {
    const wrapper = select.closest('.custom-select');
    const trigger = wrapper?.querySelector('.custom-select-trigger');

    if (!trigger) return;

    const selectedOption = select.options[select.selectedIndex];
    trigger.disabled = select.disabled;
    trigger.setAttribute('aria-disabled', String(select.disabled));
    trigger.querySelector('.ct-label').textContent =
      selectedOption?.text || '—';
    trigger.classList.toggle('is-placeholder', select.value === '');

    if (select.disabled) {
      wrapper.classList.remove('custom-select-open');
    }
  };

  document.querySelectorAll('form').forEach((form) => {
    const estado = form.querySelector('[name="estado"]');
    const calificacion = form.querySelector('[name="calificacion"]');
    const vecesVista = form.querySelector('[name="veces_vista"]');
    const favorita = form.querySelector('[name="favorita"]');
    const volveriaAVer = form.querySelector('[name="volveria_a_ver"]');
    const viewingFields = [
      calificacion,
      vecesVista,
      favorita,
      volveriaAVer
    ];

    if (!estado || viewingFields.some((field) => !field)) return;

    const syncViewingFields = () => {
      const isPending = estado.value === 'pendiente';

      if (isPending) {
        calificacion.value = '';
        vecesVista.value = '0';
        favorita.checked = false;
        volveriaAVer.checked = false;
      } else {
        const currentViews = Number.parseInt(vecesVista.value, 10);
        if (!Number.isInteger(currentViews) || currentViews < 1) {
          vecesVista.value = '1';
        }
      }

      viewingFields.forEach((field) => {
        field.disabled = isPending;
      });
      syncCustomSelect(calificacion);
    };

    syncViewingFields();
    estado.addEventListener('change', syncViewingFields);
  });
});
