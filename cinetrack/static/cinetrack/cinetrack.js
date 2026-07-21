// ======================================================
// UTILIDADES
// ======================================================

const getCookie = (name) => {
  const match = document.cookie.match(
    new RegExp(`(^|; )${name}=([^;]*)`)
  );

  return match ? decodeURIComponent(match[2]) : null;
};

const placeMenu = (trigger, menu, dir) => {
  const rect = trigger.getBoundingClientRect();
  const viewportHeight =
    window.innerHeight || document.documentElement.clientHeight;

  const espacioAbajo = viewportHeight - rect.bottom - 8;
  const espacioArriba = rect.top - 8;

  const abrirArriba = dir
    ? dir === 'up'
    : espacioAbajo < 220 && espacioArriba > espacioAbajo;

  menu.style.minWidth = `${rect.width}px`;
  menu.style.left = `${Math.round(rect.left)}px`;
  menu.style.pointerEvents = 'auto';
  menu.style.display = 'block';

  const alturaMaxima = Math.max(
    160,
    Math.min(
      380,
      abrirArriba ? espacioArriba : espacioAbajo
    )
  );

  menu.style.maxHeight = `${alturaMaxima}px`;
  menu.style.overflow = 'auto';

  if (abrirArriba) {
    menu.style.top = 'auto';
    menu.style.bottom = `${Math.round(
      viewportHeight - rect.top + 6
    )}px`;
    menu.dataset.dir = 'up';
  } else {
    menu.style.bottom = 'auto';
    menu.style.top = `${Math.round(rect.bottom + 6)}px`;
    menu.dataset.dir = 'down';
  }
};

const buildMenuFromSelect = (select, onPick) => {
  const menu = document.createElement('div');
  menu.className = 'custom-select-menu';
  menu.style.position = 'fixed';
  menu.style.display = 'none';
  menu.style.zIndex = '10000';

  Array.from(select.options).forEach((option) => {
    const item = document.createElement('div');
    item.className = 'custom-select-option';
    item.textContent = option.text;

    if (option.disabled) {
      item.setAttribute('aria-disabled', 'true');
    }

    if (option.value === '') {
      item.classList.add('is-placeholder');
    }

    if (option.selected) {
      item.setAttribute('aria-selected', 'true');
    }

    item.addEventListener('click', () => {
      if (option.disabled) return;
      onPick(option, item, menu);
    });

    menu.appendChild(item);
  });

  return menu;
};

const closeAllSelectMenus = (portal) => {
  document
    .querySelectorAll('.custom-select.custom-select-open')
    .forEach((wrapper) => wrapper.classList.remove('custom-select-open'));

  portal
    .querySelectorAll('.custom-select-menu')
    .forEach((menu) => menu.remove());
};

// ----- CATÁLOGO -----

document.addEventListener('DOMContentLoaded', () => {
  // Eliminar
  const modalEl = document.getElementById('confirmarEliminarModal');
  const tituloEl = document.getElementById('tituloAEliminar');
  const confirmBtn = document.getElementById('confirmDeleteBtn');
  let targetFormId = null;

  if (modalEl) {
    modalEl.addEventListener('show.bs.modal', (ev) => {
      const btn = ev.relatedTarget;
      if (!btn) return;
      const titulo = btn.getAttribute('data-titulo') || '';
      targetFormId = btn.getAttribute('data-form') || '';
      if (tituloEl) tituloEl.textContent = `"${titulo}"`;
    });
  }

  if (confirmBtn) {
    confirmBtn.addEventListener('click', () => {
      if (!targetFormId) return;
      const form = document.getElementById(targetFormId);
      if (form) form.submit();
    });
  }

  // Selects
  const portal = document.getElementById('ct-portal');
  if (!portal) return;

  document.querySelectorAll('.surface-card.elevated-panel select, body[data-urlname="registrar"] .elevated-panel select').forEach(sel => {
    const wrap = document.createElement('div');
    wrap.className = 'custom-select';
    sel.parentNode.insertBefore(wrap, sel);
    wrap.appendChild(sel);

    sel.style.opacity = '0';
    sel.style.position = 'absolute';
    sel.style.inset = '0';
    sel.style.width = '100%';
    sel.style.height = '100%';
    sel.style.pointerEvents = 'none';

    const trg = document.createElement('button');
    trg.type = 'button';
    trg.className = 'custom-select-trigger';
    trg.innerHTML = `<span class="ct-label">${sel.options[sel.selectedIndex]?.text || '—'}</span><span class="ct-caret"></span>`;
    trg.classList.toggle('is-placeholder', sel.value === '');
    wrap.appendChild(trg);

    trg.addEventListener('click', (ev) => {
      ev.stopPropagation();
      const wasOpen = wrap.classList.contains('custom-select-open');
      closeAllSelectMenus(portal);
      if (wasOpen) return;

      const menu = buildMenuFromSelect(sel, (opt, optionDiv, menuEl) => {
        sel.value = opt.value;
        sel.dispatchEvent(new Event('change', { bubbles: true }));
        menuEl.querySelectorAll('.custom-select-option').forEach(n => n.removeAttribute('aria-selected'));
        optionDiv.setAttribute('aria-selected', 'true');
        trg.querySelector('.ct-label').textContent = opt.text;
        trg.classList.toggle('is-placeholder', opt.value === '');
        closeAllSelectMenus(portal);
      });

      portal.appendChild(menu);
      wrap.classList.add('custom-select-open');
      placeMenu(trg, menu);
    });
  });

  const repro = () => {
    const open = document.querySelector('.custom-select.custom-select-open');
    const menu = portal.querySelector('.custom-select-menu');
    if (!open || !menu) return;
    placeMenu(open.querySelector('.custom-select-trigger'), menu, menu.dataset.dir);
  };

  window.addEventListener('scroll', repro, { passive: true });
  window.addEventListener('resize', repro, { passive: true });
  document.addEventListener('click', (e) => {
    if (e.target.closest('.custom-select')) return;
    if (portal.contains(e.target)) return;
    closeAllSelectMenus(portal);
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAllSelectMenus(portal);
  });
});


// ----- PENDIENTES -----

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.urlname || '';
  if (page !== 'pendientes') return;

  // CSRF
  const csrftoken = getCookie('csrftoken') || '';

  // Base para POST (viene del HTML; ej: "/cinetrack/mover-fase/0/")
  const moveUrlBase = document.querySelector('.page-shell')?.dataset.moveUrl || '';

  // Estado DnD
  let draggedId = null;
  let fromCol = null;

  // Placeholder
  const refreshEmpty = (col) => {
    if (!col) return;
    const items = col.querySelectorAll('[data-dnd-item]').length;
    const ph = col.querySelector('.kanban-empty-state');
    if (ph) ph.style.display = items ? 'none' : '';
  };

  // Drag & Drop
  const onDragStart = (ev) => {
    const card = ev.currentTarget;
    draggedId = card.dataset.id;
    fromCol = card.closest('[data-dnd-col]');
    ev.dataTransfer.effectAllowed = 'move';
    ev.dataTransfer.setData('text/plain', draggedId);
    card.style.opacity = 0.6;
  };

  const onDragEnd = () => {
    document.querySelectorAll('[data-dnd-item]').forEach(c => c.style.opacity = 1);
    document.querySelectorAll('[data-dnd-col]').forEach(k => k.classList.remove('kanban-column-dragover'));
  };

  const onDragOver = (ev) => {
    ev.preventDefault();
    ev.currentTarget.classList.add('kanban-column-dragover');
  };

  const onDragLeave = (ev) => {
    ev.currentTarget.classList.remove('kanban-column-dragover');
  };

  // Persistencia
  const persistMove = async (id, fase) => {
    if (!moveUrlBase) throw new Error('moveUrlBase no definido');
    const url = moveUrlBase.replace(/0\/?$/, `${id}/`);
    const resp = await fetch(url, {
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken },
      body: new URLSearchParams({ fase })
    });
    if (!resp.ok) throw new Error('HTTP ' + resp.status);
    const data = await resp.json();
    if (!data.ok) throw new Error(data.error || 'Error');
  };

  // Drop
  const onDrop = async (ev) => {
    ev.preventDefault();
    const col = ev.currentTarget;
    col.classList.remove('kanban-column-dragover');

    const fase = col.dataset.fase;
    const id = ev.dataTransfer.getData('text/plain') || draggedId;
    if (!id || !fase) return;

    const card = document.querySelector(`[data-dnd-item][data-id="${id}"]`);
    if (card) {
      if (col.firstElementChild) {
        col.insertBefore(card, col.firstElementChild);
      } else {
        col.appendChild(card);
      }
      card.style.opacity = 1;
    }

    refreshEmpty(col);
    refreshEmpty(fromCol);

    try {
      await persistMove(id, fase);
    } catch (e) {
      alert('No se pudo mover, recarga la página.');
      window.location.reload();
    }
  };

  // Inicializar
  document.querySelectorAll('[data-dnd-col]').forEach(col => {
    col.addEventListener('dragover', onDragOver);
    col.addEventListener('dragleave', onDragLeave);
    col.addEventListener('drop', onDrop);
    refreshEmpty(col);
  });

  document.querySelectorAll('[data-dnd-item]').forEach(item => {
    item.addEventListener('dragstart', onDragStart);
    item.addEventListener('dragend', onDragEnd);
  });
});


// ----- GRUPO -----

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.urlname || '';
  if (page !== 'grupo' && page !== 'grupo_saga') return;

  // Utilidades
  const csrftoken = getCookie('csrftoken') || '';

  // Base para eliminar (rendereada por Django, termina en ".../0/")
  const root = document.querySelector('[data-delete-base]');
  const deleteBase = root?.dataset.deleteBase || '';

  // Nodos del modal
  const modalEl   = document.getElementById('confirmarEliminarModal');
  const tituloEl  = document.getElementById('tituloAEliminar');
  const confirmEl = document.getElementById('confirmDeleteBtn');

  let currentId = null;
  let currentCard = null;

  if (!modalEl || !confirmEl) return;

  // Abrir modal: tomar datos del botón
  modalEl.addEventListener('show.bs.modal', (ev) => {
    const btn = ev.relatedTarget;
    if (!btn) return;
    currentId   = btn.getAttribute('data-id') || null;
    const titulo = btn.getAttribute('data-titulo') || '';
    if (tituloEl) tituloEl.textContent = `"${titulo}"`;
    currentCard = btn.closest('.col-6, .col-sm-4, .col-md-3, .col-lg-3, .col-xl-2');
  });

  // Eliminar
  confirmEl.addEventListener('click', async () => {
    if (!currentId) return;

    // Fallback: si no tenemos deleteBase, envía el form oculto
    if (!deleteBase) {
      const form = document.getElementById(`del-${currentId}`);
      if (form) form.submit();
      return;
    }

    try {
      const url = deleteBase.replace(/0\/?$/, `${currentId}/`);
      const resp = await fetch(url, {
        method: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest', 'X-CSRFToken': csrftoken },
      });

      const isJSON = (resp.headers.get('content-type') || '').includes('application/json');
      const data = isJSON ? await resp.json() : null;

      if (resp.ok && data && data.ok) {
        // Quitar card
        if (currentCard && currentCard.parentNode) currentCard.parentNode.removeChild(currentCard);

        // Actualizar contador del subtítulo
        const sub = document.querySelector('.hero-sub');
        if (sub) {
          const m = sub.textContent.match(/(\d+)/);
          if (m) sub.textContent = sub.textContent.replace(/\d+/, String(Math.max(0, (parseInt(m[1],10)||1) - 1)));
        }

        // Cerrar modal
        (bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl)).hide();
      } else {
        // Fallback: si el backend no devolvió JSON OK, usa form estándar
        const form = document.getElementById(`del-${currentId}`);
        if (form) return form.submit();
        alert('No se pudo eliminar. Intenta de nuevo.');
      }
    } catch (e) {
      alert('Error de red. Vuelve a intentarlo.');
    }
  });
});


// ----- MARATONES (listado) -----
(function () {
  function setupMaratonesDeleteModal() {
    const modal = document.getElementById('confirmarEliminarModal');
    if (!modal || modal.dataset.bound === '1') return; // evitar doble binding

    const tituloEl  = modal.querySelector('#tituloAEliminar');
    const confirmEl = modal.querySelector('#confirmDeleteBtn');
    let targetFormId = null;

    // Cuando se abre el modal, leer data-* del botón que lo abrió
    modal.addEventListener('show.bs.modal', (ev) => {
      const trigger = ev.relatedTarget;
      if (!(trigger instanceof HTMLElement)) return;
      targetFormId = trigger.getAttribute('data-form') || null;
      const titulo = trigger.getAttribute('data-titulo') || '—';
      if (tituloEl) tituloEl.textContent = `«${titulo}»`;
    });

    // Confirmar: enviar el form oculto
    confirmEl?.addEventListener('click', () => {
      if (!targetFormId) return;
      const form = document.getElementById(targetFormId);
      form?.submit();
    });

    modal.dataset.bound = '1';
  }

  if (document.readyState !== 'loading') setupMaratonesDeleteModal();
  else document.addEventListener('DOMContentLoaded', setupMaratonesDeleteModal);
})();

// ----- MARATONES (form) -----
(function () {
  function initMaratonForm() {
    const grid = document.getElementById('contenidos-grid');
    if (!grid || grid.dataset.bound === '1') return; // ya inicializado o no es esta página
    grid.dataset.bound = '1';

    // --- Glow de seleccionados ---
    const boxes = grid.querySelectorAll('input[type="checkbox"][name="contenidos"]');
    const countEl = document.getElementById('seleccionados-count');

    const actualizarConteo = () => {
      if (!countEl) return;

      const total = Array.from(boxes).filter((cb) => cb.checked).length;
      countEl.textContent = total;
    };
    boxes.forEach((cb) => {
      const card = grid.querySelector(`label[for="${cb.id}"]`);
      const sync = () => {
        if (card) {
          card.classList.toggle('marathon-selection-selected', cb.checked);
        }
        actualizarConteo();
      };
      sync();                    // estado inicial
      cb.addEventListener('change', sync);
    });

    // --- Filtro (botón + Enter) sin enviar el form ---
    const input = document.getElementById('filtro-contenidos');
    const btn   = document.getElementById('btn-filtrar');

    function aplicarFiltro() {
      const term = (input?.value || '').toLowerCase();
      grid.querySelectorAll('.col-6, .col-sm-4, .col-md-3, .col-lg-2').forEach((col) => {
        const title = (col.querySelector('.small')?.innerText || '').toLowerCase();
        col.style.display = title.includes(term) ? '' : 'none';
      });
    }

    btn?.addEventListener('click', aplicarFiltro);
    input?.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') { e.preventDefault(); aplicarFiltro(); }
    });
  }

  if (document.readyState !== 'loading') initMaratonForm();
  else document.addEventListener('DOMContentLoaded', initMaratonForm);

  // opcional: disponible por si recargas contenido dinámicamente
  window._ctInitMaratonForm = initMaratonForm;
})();


// ----- MARATONES (detalle) -----
(function () {
  // guarda el último botón que abrió el modal (fallback si relatedTarget viene vacío)
  let lastTrigger = null;
  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-bs-target="#confirmarQuitarModal"]');
    if (t) lastTrigger = t;
  }, true); // en captura para correr antes que Bootstrap

  function initFiltro() {
    const grid  = document.getElementById('mara-grid');
    const input = document.getElementById('filtro-mara');
    const btn   = document.getElementById('btn-filtrar-mara');
    const count = document.getElementById('mara-count');
    if (!grid || grid.dataset.filterBound === '1') return;
    grid.dataset.filterBound = '1';

    function aplicar() {
      const term = (input?.value || '').toLowerCase();
      let visibles = 0;
      grid.querySelectorAll('.col-6, .col-sm-4, .col-md-3, .col-lg-3, .col-xl-2').forEach(col => {
        const title = (col.querySelector('.top-card-name')?.innerText || '').toLowerCase();
        const show = title.includes(term);
        col.style.display = show ? '' : 'none';
        if (show) visibles++;
      });
      if (count) count.textContent = `${visibles} títulos`;
    }

    btn?.addEventListener('click', aplicar);
    input?.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); aplicar(); } });
    input?.addEventListener('input', aplicar);
  }

  function initQuitarModal() {
    const modal = document.getElementById('confirmarQuitarModal');
    if (!modal || modal.dataset.bound === '1') return;
    modal.dataset.bound = '1';

    const tituloEl  = modal.querySelector('#tituloAQuitar');
    const confirmEl = modal.querySelector('#confirmQuitarBtn');
    let targetFormId = null;

    // Bootstrap pasa el botón en relatedTarget; si no, usamos lastTrigger
    modal.addEventListener('show.bs.modal', (ev) => {
      const trigger = ev.relatedTarget || lastTrigger || document.activeElement;
      if (trigger && trigger.getAttribute) {
        targetFormId = trigger.getAttribute('data-form') || null;
        const titulo = trigger.getAttribute('data-titulo') || '—';
        if (tituloEl) tituloEl.textContent = `«${titulo}»`;
      } else {
        targetFormId = null;
        if (tituloEl) tituloEl.textContent = '—';
      }
    });

    confirmEl?.addEventListener('click', () => {
      if (!targetFormId) return;
      document.getElementById(targetFormId)?.submit();
    });
  }

  function init() {
    initFiltro();
    initQuitarModal();
  }

  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);

  // por si reinyectas contenido dinámicamente
  window._ctInitMaratonDetalle = init;
})();
