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
  const portalId = 'ct-portal';
  let portal = document.getElementById(portalId);
  if (!portal) {
    portal = document.createElement('div');
    portal.id = portalId;
    portal.style.position = 'fixed';
    portal.style.inset = '0';
    portal.style.zIndex = '9999';
    portal.style.pointerEvents = 'none';
    document.body.appendChild(portal);
  }

  function placeMenu(trigger, menu, dir) {
    const r = trigger.getBoundingClientRect();
    const vpH = window.innerHeight || document.documentElement.clientHeight;
    const below = vpH - r.bottom - 8;
    const above = r.top - 8;
    const openUp = dir ? dir === 'up' : (below < 220 && above > below);

    menu.style.minWidth = r.width + 'px';
    menu.style.left = Math.round(r.left) + 'px';
    menu.style.pointerEvents = 'auto';
    menu.style.display = 'block';

    const maxH = Math.max(160, Math.min(380, openUp ? above : below));
    menu.style.maxHeight = maxH + 'px';
    menu.style.overflow = 'auto';

    if (openUp) {
      menu.style.top = 'auto';
      menu.style.bottom = Math.round(vpH - r.top + 6) + 'px';
      menu.dataset.dir = 'up';
    } else {
      menu.style.bottom = 'auto';
      menu.style.top = Math.round(r.bottom + 6) + 'px';
      menu.dataset.dir = 'down';
    }
  }

  function closeAll() {
    document.querySelectorAll('.ct-select.ct-open').forEach(w => w.classList.remove('ct-open'));
    portal.querySelectorAll('.ct-menu').forEach(m => m.remove());
  }

  function buildMenuFromSelect(sel, onPick) {
    const menu = document.createElement('div');
    menu.className = 'ct-menu';
    menu.style.position = 'fixed';
    menu.style.display = 'none';
    menu.style.zIndex = '10000';

    Array.from(sel.options).forEach(opt => {
      const o = document.createElement('div');
      o.className = 'ct-option';
      o.textContent = opt.text;
      if (opt.disabled) o.setAttribute('aria-disabled', 'true');
      if (opt.value === '') o.classList.add('is-placeholder');
      if (opt.selected)  o.setAttribute('aria-selected', 'true');
      o.addEventListener('click', () => {
        if (opt.disabled) return;
        onPick(opt, o, menu);
      });
      menu.appendChild(o);
    });

    return menu;
  }

  document.querySelectorAll('.tile.edit-card select').forEach(sel => {
    const wrap = document.createElement('div');
    wrap.className = 'ct-select';
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
    trg.className = 'ct-trigger';
    trg.innerHTML = `<span class="ct-label">${sel.options[sel.selectedIndex]?.text || '—'}</span><span class="ct-caret"></span>`;
    wrap.appendChild(trg);

    trg.addEventListener('click', (ev) => {
      ev.stopPropagation();
      const wasOpen = wrap.classList.contains('ct-open');
      closeAll();
      if (wasOpen) return;

      const menu = buildMenuFromSelect(sel, (opt, optionDiv, menuEl) => {
        sel.value = opt.value;
        sel.dispatchEvent(new Event('change', { bubbles: true }));
        menuEl.querySelectorAll('.ct-option').forEach(n => n.removeAttribute('aria-selected'));
        optionDiv.setAttribute('aria-selected', 'true');
        trg.querySelector('.ct-label').textContent = opt.text;
        closeAll();
      });

      portal.appendChild(menu);
      wrap.classList.add('ct-open');
      placeMenu(trg, menu);
    });
  });

  const repro = () => {
    const open = document.querySelector('.ct-select.ct-open');
    const menu = portal.querySelector('.ct-menu');
    if (!open || !menu) return;
    placeMenu(open.querySelector('.ct-trigger'), menu, menu.dataset.dir);
  };

  window.addEventListener('scroll', repro, { passive: true });
  window.addEventListener('resize', repro, { passive: true });
  document.addEventListener('click', (e) => {
    if (e.target.closest('.ct-select')) return;
    if (portal.contains(e.target)) return;
    closeAll();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAll();
  });
});


// ----- PENDIENTES -----

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.urlname || '';
  if (page !== 'pendientes') return;

  // CSRF
  const getCookie = (name) => {
    const m = document.cookie.match(new RegExp('(^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[2]) : null;
  };
  const csrftoken = getCookie('csrftoken') || '';

  // Base para POST (viene del HTML; ej: "/cinetrack/mover-fase/0/")
  const moveUrlBase = document.querySelector('.edit-page')?.dataset.moveUrl || '';

  // Estado DnD
  let draggedId = null;
  let fromCol = null;

  // Placeholder
  const refreshEmpty = (col) => {
    if (!col) return;
    const items = col.querySelectorAll('[data-dnd-item]').length;
    const ph = col.querySelector('.kan-empty');
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
    document.querySelectorAll('[data-dnd-col]').forEach(k => k.classList.remove('col-dragover'));
  };

  const onDragOver = (ev) => {
    ev.preventDefault();
    ev.currentTarget.classList.add('col-dragover');
  };

  const onDragLeave = (ev) => {
    ev.currentTarget.classList.remove('col-dragover');
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
    col.classList.remove('col-dragover');

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
  const getCookie = (name) => {
    const m = document.cookie.match(new RegExp('(^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[2]) : null;
  };
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


// ----- REGISTRAR -----
document.addEventListener('DOMContentLoaded', () => {
  const urlname = document.body.dataset.urlname || '';
  if (urlname !== 'registrar') return;

  // Portal único para menús
  let portal = document.getElementById('ct-portal');
  if (!portal) {
    portal = document.createElement('div');
    portal.id = 'ct-portal';
    Object.assign(portal.style, { position:'fixed', inset:'0', zIndex:'9999', pointerEvents:'none' });
    document.body.appendChild(portal);
  }

  const placeMenu = (trigger, menu, dir) => {
    const r = trigger.getBoundingClientRect();
    const vpH = window.innerHeight || document.documentElement.clientHeight;
    const below = vpH - r.bottom - 8, above = r.top - 8;
    const openUp = dir ? dir === 'up' : (below < 220 && above > below);
    menu.style.minWidth = r.width + 'px';
    menu.style.left = Math.round(r.left) + 'px';
    menu.style.pointerEvents = 'auto';
    menu.style.display = 'block';
    const maxH = Math.max(160, Math.min(380, openUp ? above : below));
    menu.style.maxHeight = maxH + 'px';
    menu.style.overflow = 'auto';
    if (openUp) {
      menu.style.top = 'auto';
      menu.style.bottom = Math.round(vpH - r.top + 6) + 'px';
      menu.dataset.dir = 'up';
    } else {
      menu.style.bottom = 'auto';
      menu.style.top = Math.round(r.bottom + 6) + 'px';
      menu.dataset.dir = 'down';
    }
  };

  const closeAll = () => {
    document.querySelectorAll('.ct-select.ct-open').forEach(w => w.classList.remove('ct-open'));
    portal.querySelectorAll('.ct-menu').forEach(m => m.remove());
  };

  const buildMenuFromSelect = (sel, onPick) => {
    const menu = document.createElement('div');
    menu.className = 'ct-menu';
    Object.assign(menu.style, { position:'fixed', display:'none' });
    Array.from(sel.options).forEach(opt => {
      const o = document.createElement('div');
      o.className = 'ct-option';
      o.textContent = opt.text;
      if (opt.disabled) o.setAttribute('aria-disabled', 'true');
      if (opt.value === '') o.classList.add('is-placeholder');
      if (opt.selected)  o.setAttribute('aria-selected', 'true');
      o.addEventListener('click', () => { if (!opt.disabled) onPick(opt, o, menu); });
      menu.appendChild(o);
    });
    return menu;
  };

  // Mejora los selects del formulario de Registrar
  document.querySelectorAll('.edit-card select').forEach(sel => {
    const wrap = document.createElement('div');
    wrap.className = 'ct-select';
    sel.parentNode.insertBefore(wrap, sel);
    wrap.appendChild(sel);

    // Oculta el select real
    Object.assign(sel.style, { opacity:'0', position:'absolute', inset:'0', width:'100%', height:'100%', pointerEvents:'none' });

    // Trigger
    const trg = document.createElement('button');
    trg.type = 'button';
    trg.className = 'ct-trigger';
    trg.innerHTML = `<span class="ct-label">${sel.options[sel.selectedIndex]?.text || '—'}</span><span class="ct-caret"></span>`;
    wrap.appendChild(trg);

    trg.addEventListener('click', (ev) => {
      ev.stopPropagation();
      const wasOpen = wrap.classList.contains('ct-open');
      closeAll();
      if (wasOpen) return;

      const menu = buildMenuFromSelect(sel, (opt, optionDiv, menuEl) => {
        sel.value = opt.value;
        sel.dispatchEvent(new Event('change', { bubbles:true }));
        menuEl.querySelectorAll('.ct-option').forEach(n => n.removeAttribute('aria-selected'));
        optionDiv.setAttribute('aria-selected', 'true');
        trg.querySelector('.ct-label').textContent = opt.text;
        closeAll();
      });

      portal.appendChild(menu);
      wrap.classList.add('ct-open');
      placeMenu(trg, menu);
    });
  });

  const repro = () => {
    const open = document.querySelector('.ct-select.ct-open');
    const menu = portal.querySelector('.ct-menu');
    if (!open || !menu) return;
    placeMenu(open.querySelector('.ct-trigger'), menu, menu.dataset.dir);
  };
  window.addEventListener('scroll', repro, { passive:true });
  window.addEventListener('resize', repro, { passive:true });
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.ct-select') && !portal.contains(e.target)) closeAll();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeAll(); });
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
    boxes.forEach((cb) => {
      const card = grid.querySelector(`label[for="${cb.id}"]`);
      const sync = () => card && card.classList.toggle('selected', cb.checked);
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
// ===== MARATON · DETALLE (robusto) =====
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
        const title = (col.querySelector('.topcard-name')?.innerText || '').toLowerCase();
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
