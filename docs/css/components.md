## css/components/buttons.css

```css
.btn-center {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
}
```

`display: inline-flex`: mantiene el botón en línea y organiza su contenido mediante Flexbox.

`align-items: center`: centra verticalmente el contenido del botón.

`justify-content: center`: centra horizontalmente el contenido.

`gap: .5rem`: deja medio `rem` de separación entre los elementos internos.

---

```css
.btn-center i {
  flex: 0 0 auto;
}
```

`flex: 0 0 auto`: evita que el icono crezca o se reduzca dentro del botón y conserva su tamaño natural.

---

```css
.btn-neon {
  --c1: var(--accent);
  --c2: var(--color-accent-dark);
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  color: #fff;
  text-decoration: none;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--c1), var(--c2));
  padding: .8rem 1.1rem;
  font-weight: 700;
  box-shadow: 0 10px 24px rgba(111,63,230,.35),
              inset 0 0 0 1px rgba(255,255,255,.08);
  transition: transform .15s ease,
              box-shadow .2s ease,
              filter .2s ease;
}
```

`--c1: var(--accent)`: guarda localmente en `--c1` el morado claro `#9b5cfb` definido por `--accent`.

`--c2: var(--color-accent-dark)`: guarda localmente en `--c2` el morado oscuro `#6f3fe6` definido por `--color-accent-dark`.

`display: inline-flex`: mantiene el botón en línea y organiza su contenido con Flexbox.

`align-items: center`: centra verticalmente el icono y el texto.

`gap: .5rem`: separa los elementos internos por medio `rem`.

`color: #fff`: muestra el texto y los iconos en blanco.

`text-decoration: none`: elimina el subrayado cuando el componente se utiliza como enlace.

`border: none`: elimina cualquier borde propio del elemento.

`border-radius: 12px`: redondea las esquinas del botón.

`background`: crea un degradado diagonal desde `--c1` hasta `--c2`.

`padding: .8rem 1.1rem`: añade `0.8rem` de espacio vertical y `1.1rem` horizontal.

`font-weight: 700`: muestra el texto en negrita.

`box-shadow`: proyecta una sombra morada con 35 % de opacidad y dibuja una línea blanca interior con 8 % de opacidad.

`transition`: suaviza los cambios de posición durante 0.15 segundos y los cambios de sombra y brillo durante 0.2 segundos.

---

```css
.btn-neon:hover {
  color: #fff;
  transform: translateY(-1px);
  filter: brightness(1.06);
  box-shadow: 0 14px 30px rgba(111,63,230,.45);
}
```

`color: #fff`: mantiene el contenido en blanco al pasar el cursor.

`transform: translateY(-1px)`: eleva el botón un píxel.

`filter: brightness(1.06)`: aumenta su brillo un 6 %.

`box-shadow`: amplía la sombra morada y aumenta su opacidad al 45 %.

---

```css
.btn-neon.small {
  padding: .55rem .8rem;
  border-radius: 10px;
  font-size: .95rem;
}
```

`padding: .55rem .8rem`: reduce el espacio interno a `0.55rem` vertical y `0.8rem` horizontal.

`border-radius: 10px`: reduce ligeramente el redondeo de las esquinas.

`font-size: .95rem`: muestra el texto al 95 % del tamaño base.

---

```css
.btn-ghost {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  color: #e9d5ff;
  text-decoration: none;
  border: 1px solid var(--color-border-subtle);
  border-radius: 12px;
  background: rgba(255,255,255,.04);
  padding: .8rem 1.1rem;
  backdrop-filter: blur(4px);
  transition: all .18s ease;
}
```

`display: inline-flex`: mantiene el botón en línea y distribuye su contenido con Flexbox.

`align-items: center`: centra verticalmente sus elementos internos.

`gap: .5rem`: deja medio `rem` entre el icono y el texto.

`color: #e9d5ff`: aplica un lavanda muy claro al contenido.

`text-decoration: none`: elimina el subrayado si el botón es un enlace.

`border: 1px solid var(--color-border-subtle)`: dibuja un borde tenue con `--color-border-subtle`, cuyo valor actual es `rgba(255,255,255,.12)`.

`border-radius: 12px`: redondea las esquinas.

`background`: aplica un fondo blanco con 4 % de opacidad.

`padding: .8rem 1.1rem`: añade `0.8rem` de espacio vertical y `1.1rem` horizontal.

`backdrop-filter: blur(4px)`: desenfoca cuatro píxeles el contenido situado detrás.

`transition: all .18s ease`: suaviza durante 0.18 segundos cualquier propiedad que cambie.

---

```css
.btn-ghost:hover {
  color: #fff;
  background: rgba(255,255,255,.08);
  border-color: rgba(255,255,255,.22);
}
```

`color: #fff`: cambia el contenido a blanco al pasar el cursor.

`background`: aumenta la opacidad del fondo blanco al 8 %.

`border-color`: aumenta la opacidad del borde blanco al 22 %.

---

```css
.btn-ghost-sm {
  color: inherit;
  text-decoration: none;
  padding: .45rem .6rem;
  border-radius: 10px;
  border: 1px solid var(--color-border-subtle);
  background: rgba(255,255,255,.04);
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-weight: 500;
  transition: all .15s ease;
}
```

`color: inherit`: usa el color de texto heredado del elemento contenedor.

`text-decoration: none`: elimina el subrayado cuando se utiliza como enlace.

`padding: .45rem .6rem`: añade `0.45rem` de espacio vertical y `0.6rem` horizontal.

`border-radius: 10px`: redondea las esquinas.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde tenue definido por `--color-border-subtle`, actualmente `rgba(255,255,255,.12)`.

`background`: aplica un fondo blanco con 4 % de opacidad.

`display: inline-flex`: mantiene el componente en línea y organiza su contenido con Flexbox.

`align-items: center`: centra verticalmente sus elementos.

`gap: .4rem`: deja `0.4rem` entre los elementos internos.

`font-weight: 500`: aplica un grosor medio al texto.

`transition: all .15s ease`: suaviza durante 0.15 segundos cualquier propiedad que cambie.

---

```css
.btn-ghost-sm:hover {
  color: #fff;
  background: rgba(255,255,255,.08);
}
```

`color: #fff`: muestra el contenido en blanco al pasar el cursor.

`background`: aumenta la opacidad del fondo blanco al 8 %.

---

```css
.btn-save {
  --c1: var(--accent);
  --c2: var(--color-accent-dark);
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .8rem 1.2rem;
  font-weight: 900;
  letter-spacing: .2px;
  border-radius: 12px;
  border: 1px solid transparent;
  color: #fff;
  text-decoration: none;
  background: linear-gradient(135deg, var(--c1), var(--c2));
  box-shadow: 0 0 14px rgba(111,63,230,.55), inset 0 0 0 1px rgba(255,255,255,.08);
  transition: transform .12s ease, box-shadow .18s ease, filter .12s ease;
  animation: pulseGlow 2.2s ease-in-out infinite;
}
```

`--c1: var(--accent)`: asigna localmente a `--c1` el morado claro `#9b5cfb`.

`--c2: var(--color-accent-dark)`: asigna localmente a `--c2` el morado oscuro `#6f3fe6`.

`display: inline-flex`: mantiene el botón en línea y organiza su contenido con Flexbox.

`align-items: center`: centra verticalmente sus elementos.

`gap: .55rem`: separa los elementos internos por `0.55rem`.

`padding: .8rem 1.2rem`: añade `0.8rem` de espacio vertical y `1.2rem` horizontal.

`font-weight: 900`: aplica el grosor más intenso disponible de la tipografía.

`letter-spacing: .2px`: separa las letras por 0.2 píxeles.

`border-radius: 12px`: redondea las esquinas.

`border: 1px solid transparent`: reserva un borde transparente de un píxel sin añadir color visible.

`color: #fff`: muestra el contenido en blanco.

`text-decoration: none`: elimina el subrayado si el botón es un enlace.

`background`: crea un degradado diagonal entre los dos colores morados locales.

`box-shadow`: genera un resplandor morado con 55 % de opacidad y una línea blanca interior con 8 % de opacidad.

`transition`: suaviza los cambios de posición y brillo durante 0.12 segundos y los de sombra durante 0.18 segundos.

`animation`: ejecuta `pulseGlow` continuamente, con ciclos de 2.2 segundos y aceleración suave al inicio y al final.

---

```css
.btn-save:hover {
  color: #fff;
  transform: translateY(-1px);
  box-shadow: 0 0 18px rgba(155,92,251,.7);
  filter: brightness(1.06);
}
```

`color: #fff`: mantiene el contenido en blanco al pasar el cursor.

`transform: translateY(-1px)`: eleva el botón un píxel.

`box-shadow`: amplía el resplandor y usa el morado `rgba(155,92,251,.7)` con 70 % de opacidad.

`filter: brightness(1.06)`: aumenta el brillo del botón un 6 %.

---

```css
.btn-glow {
  --c1: var(--accent, #9b5cfb);
  --c2: var(--color-accent-dark, #6f3fe6);
  border: 1px solid transparent;
  background: linear-gradient(135deg, var(--c1), var(--c2));
  color: #fff;
  font-weight: 800;
  box-shadow: 0 0 14px rgba(155,92,251,.55), inset 0 0 0 1px rgba(255,255,255,.08);
}
```

`--c1`: usa `--accent`, actualmente `#9b5cfb`, con ese mismo respaldo.

`--c2`: usa `--color-accent-dark`, actualmente `#6f3fe6`, con ese mismo respaldo.

`border`: reserva un borde transparente de un píxel.

`background`: crea un degradado diagonal entre ambos morados.

`color: #fff`: muestra el contenido en blanco.

`font-weight: 800`: aplica un grosor intenso.

`box-shadow`: añade un resplandor morado y una línea blanca interior.

---

```css
.btn-glow:hover {
  filter: brightness(1.06);
  box-shadow: 0 0 18px rgba(155,92,251,.7);
}
```

`filter`: aumenta el brillo un 6 %.

`box-shadow`: amplía el resplandor morado y aumenta su opacidad al 70 %.

## css/components/badges.css

```css
.badge.tipo {
  background: linear-gradient(135deg, #9b5cfb, #6f3fe6);
  color: #fff;
  font-weight: 700;
}
```

`background`: crea un degradado diagonal desde el morado claro `#9b5cfb` hasta el morado oscuro `#6f3fe6`.

`color: #fff`: muestra el texto en blanco.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.plataforma {
  background-color: #00b4d8;
  color: #fff;
  font-weight: 700;
}
```

`background-color: #00b4d8`: aplica un fondo cian intenso.

`color: #fff`: muestra el texto en blanco.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.estado-vista {
  background-color: #ff9914;
  color: #fff;
  font-weight: 700;
}
```

`background-color: #ff9914`: aplica un fondo naranja a la insignia del estado visto.

`color: #fff`: muestra el texto en blanco.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.estado-pendiente {
  background-color: #dc3545;
  color: #fff;
  font-weight: 700;
}
```

`background-color: #dc3545`: aplica un fondo rojo a la insignia del estado pendiente.

`color: #fff`: muestra el texto en blanco.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.busqueda {
  background: #5f0f40;
  color: #fff;
}
```

`background: #5f0f40`: aplica un fondo vino oscuro a la insignia de búsqueda.

`color: #fff`: muestra el texto en blanco.

---

```css
.badge.cal-excelente {
  background-color: #2b9348;
  color: #fff;
  font-weight: 700;
}
```

`background-color: #2b9348`: aplica un fondo verde oscuro para una calificación excelente.

`color: #fff`: muestra el texto en blanco.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.cal-buena {
  background-color: #80b918;
  color: #fff;
  font-weight: 700;
}
```

`background-color: #80b918`: aplica un fondo verde claro para una calificación buena.

`color: #fff`: muestra el texto en blanco.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.cal-regular {
  background-color: #bfd200;
  color: #000;
  font-weight: 700;
}
```

`background-color: #bfd200`: aplica un fondo verde amarillento para una calificación regular.

`color: #000`: muestra el texto en negro para contrastar con el fondo claro.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.cal-mala {
  background-color: #d4d700;
  color: #000;
  font-weight: 700;
}
```

`background-color: #d4d700`: aplica un fondo amarillo verdoso para una calificación mala.

`color: #000`: muestra el texto en negro para contrastar con el fondo.

`font-weight: 700`: aplica negrita al texto.

---

```css
.badge.cal-horrible {
  background-color: #ffff3f;
  color: #000;
  font-weight: 700;
}
```

`background-color: #ffff3f`: aplica un fondo amarillo brillante para una calificación horrible.

`color: #000`: muestra el texto en negro para mantener el contraste.

`font-weight: 700`: aplica negrita al texto.

---

```css
.favorite-star {
  color: #ffd700;
  filter: drop-shadow(0 0 6px rgba(255, 215, 0, 0.45));
}
```

`color: #ffd700`: muestra la estrella en dorado.

`filter`: añade un resplandor dorado difuminado de seis píxeles con 45 % de opacidad.

## css/components/section-titles.css

```css
.section-title {
  margin: 0;
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .6px;
  color: var(--color-text-secondary);
  display: flex;
  align-items: center;
  gap: .5rem;
}
```

`margin: 0`: elimina el margen exterior predeterminado del título.

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz, cuyo valor actual es `'Teko', system-ui, sans-serif`.

`text-transform: uppercase`: muestra el texto en mayúsculas.

`letter-spacing: .6px`: separa las letras por 0.6 píxeles.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb` definido actualmente por `--color-text-secondary`.

`display: flex`: organiza los elementos internos del título mediante Flexbox.

`align-items: center`: centra verticalmente el texto y cualquier icono asociado.

`gap: .5rem`: deja medio `rem` entre los elementos internos.

## css/components/surfaces.css

```css
.edit-card {
  background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04));
  border: 1px solid var(--color-border-subtle);
  border-radius: 20px;
  box-shadow: 0 18px 36px rgba(0,0,0,.45);
  backdrop-filter: blur(8px) saturate(135%);
  animation: floatUp .45s ease both;
  position: relative;
  overflow: hidden;
}
```

`background`: crea un degradado vertical blanco semitransparente, del 8 % de opacidad arriba al 4 % abajo.

`border: 1px solid var(--color-border-subtle)`: dibuja un borde tenue con `--color-border-subtle`, cuyo valor actual es `rgba(255,255,255,.12)`.

`border-radius: 20px`: redondea las esquinas de la superficie.

`box-shadow`: proyecta una sombra negra con 45 % de opacidad, desplazada 18 píxeles hacia abajo y difuminada 36 píxeles.

`backdrop-filter`: desenfoca ocho píxeles el contenido situado detrás y aumenta su saturación al 135 %.

`animation`: ejecuta `floatUp` durante 0.45 segundos, conserva tanto el estado inicial como el final de la animación y utiliza una aceleración suave.

`position: relative`: convierte la superficie en la referencia de posicionamiento de su pseudoelemento `::after`.

`overflow: hidden`: recorta el pseudoelemento y cualquier contenido que sobresalga de las esquinas redondeadas.

---

```css
.edit-card::after {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 20px;
  pointer-events: none;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.08), 0 0 32px rgba(155,92,251,.18);
}
```

`content: ""`: crea un pseudoelemento vacío para dibujar el acabado luminoso.

`position: absolute`: permite cubrir la superficie sin alterar el flujo del contenido.

`inset: -1px`: extiende el pseudoelemento un píxel más allá de cada borde.

`border-radius: 20px`: mantiene el mismo redondeo que la superficie.

`pointer-events: none`: evita que el acabado intercepte clics o movimientos del puntero.

`box-shadow`: dibuja una línea blanca interior con 8 % de opacidad y un resplandor morado exterior con 18 % de opacidad.

## css/components/forms.css

```css
.form-label {
  margin-bottom: .35rem;
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .5px;
  color: var(--color-text-secondary);
  font-weight: 700;
}
```

`margin-bottom: .35rem`: separa la etiqueta del control inferior.

`font-family: var(--font-family-interface)`: usa la tipografía de interfaz `'Teko', system-ui, sans-serif`.

`text-transform: uppercase`: muestra el texto en mayúsculas.

`letter-spacing: .5px`: separa las letras medio píxel.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb`.

`font-weight: 700`: muestra la etiqueta en negrita.

---

```css
.edit-form input[type="text"],
.edit-form input[type="number"],
.edit-form input[type="date"],
.edit-form select,
.edit-form textarea {
  width: 100%;
  color: var(--color-text-primary);
  background: rgba(255,255,255,.05);
  border: 1px solid var(--color-border-subtle);
  border-radius: 12px;
  padding: .7rem .9rem;
  outline: none;
  transition: box-shadow .18s ease, border-color .18s ease, background .18s ease, transform .12s ease;
}
```

`width: 100%`: extiende los controles al ancho disponible.

`color: var(--color-text-primary)`: aplica el color principal `#f6f3ff`.

`background`: usa un fondo blanco con 5 % de opacidad.

`border`: aplica el borde tenue definido por `--color-border-subtle`.

`border-radius: 12px`: redondea las esquinas.

`padding`: añade `0.7rem` vertical y `0.9rem` horizontal.

`outline: none`: elimina el contorno nativo de enfoque.

`transition`: suaviza los cambios de sombra, borde, fondo y posición.

---

```css
.edit-form input:hover,
.edit-form select:hover,
.edit-form textarea:hover {
  background: rgba(255,255,255,.06);
}
```

`background`: aumenta el fondo blanco al 6 % de opacidad al pasar el cursor.

---

```css
.edit-form input:focus,
.edit-form select:focus,
.edit-form textarea:focus {
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(155,92,251,.45), 0 0 16px rgba(111,63,230,.4);
  transform: translateY(-1px);
}
```

`border-color: transparent`: oculta el color del borde durante el enfoque.

`box-shadow`: dibuja un anillo y un resplandor morados alrededor del control.

`transform`: eleva el control un píxel.

---

```css
.edit-form input[readonly] {
  opacity: .9;
  background: rgba(255,255,255,.04);
}
```

`opacity: .9`: reduce ligeramente la opacidad del campo de solo lectura.

`background`: aplica un fondo blanco con 4 % de opacidad.

---

```css
.edit-form textarea {
  min-height: 140px;
  resize: vertical;
  line-height: 1.55;
  font-weight: 500;
  background-image:
    linear-gradient(rgba(255,255,255,.04), rgba(255,255,255,.04)),
    repeating-linear-gradient(to bottom,
      rgba(255,255,255,.05) 0 32px,
      rgba(255,255,255,.06) 32px 33px);
  background-clip: padding-box;
}
```

`min-height: 140px`: impide que el área sea más baja que 140 píxeles.

`resize: vertical`: permite cambiar únicamente su altura.

`line-height: 1.55`: separa las líneas a 1.55 veces el tamaño de fuente.

`font-weight: 500`: aplica un grosor medio.

`background-image`: superpone un fondo blanco tenue y líneas horizontales repetidas cada 33 píxeles.

`background-clip: padding-box`: limita el fondo al área interior del borde.

---

```css
.edit-form textarea.form-control,
.edit-form textarea {
  background-color: transparent;
  color: #f6f3ff;
}
```

`background-color: transparent`: mantiene transparente el color de fondo frente a Bootstrap.

`color: #f6f3ff`: muestra el texto en blanco lavanda.

---

```css
.edit-form textarea.form-control::placeholder {
  color: rgba(246,243,255,.55);
}
```

`color`: muestra el marcador de posición en blanco lavanda con 55 % de opacidad.

---

```css
.edit-form textarea.form-control:focus {
  background-color: transparent;
  border-color: rgba(180,70,255,.6);
  box-shadow: 0 0 0 .25rem rgba(180,70,255,.15);
  outline: none;
}
```

`background-color: transparent`: conserva el fondo transparente durante el enfoque.

`border-color`: aplica un borde morado con 60 % de opacidad.

`box-shadow`: añade un anillo morado de `0.25rem` con 15 % de opacidad.

`outline: none`: elimina el contorno nativo.

---

```css
.form-check.form-switch .form-check-input {
  width: 46px;
  height: 26px;
  cursor: pointer;
  background-color: rgba(255,255,255,.14);
  border: 1px solid var(--color-border-subtle);
  transition: box-shadow .18s ease, filter .18s ease;
}
```

`width: 46px` y `height: 26px`: fijan las dimensiones del interruptor.

`cursor: pointer`: muestra que el control es interactivo.

`background-color`: aplica un fondo blanco con 14 % de opacidad.

`border`: utiliza el borde tenue definido por `--color-border-subtle`.

`transition`: suaviza los cambios de sombra y filtro durante 0.18 segundos.

---

```css
.form-check.form-switch .form-check-input:focus {
  box-shadow: 0 0 0 3px rgba(155,92,251,.35);
}
```

`box-shadow`: dibuja un anillo morado de tres píxeles al enfocar el interruptor.

---

```css
.form-check-label {
  font-weight: 700;
  color: var(--color-text-primary);
  opacity: .92;
}
```

`font-weight: 700`: muestra la etiqueta en negrita.

`color: var(--color-text-primary)`: aplica el blanco lavanda `#f6f3ff`.

`opacity: .92`: muestra la etiqueta con 92 % de opacidad.

---

```css
#id_favorita.form-check-input:checked {
  background-color: #ffd700;
  border-color: rgba(0,0,0,.15);
}
```

`background-color: #ffd700`: muestra en dorado el interruptor de favorita activado.

`border-color`: aplica un borde negro con 15 % de opacidad.

---

```css
#id_volveria_a_ver.form-check-input:checked {
  background-color: #1e90ff;
  border-color: rgba(0,0,0,.15);
}
```

`background-color: #1e90ff`: muestra en azul el interruptor de volvería a ver activado.

`border-color`: aplica un borde negro con 15 % de opacidad.

---

```css
#id_tendra_continuacion.form-check-input:checked {
  background-color: #2ecc71;
  border-color: rgba(0,0,0,.15);
}
```

`background-color: #2ecc71`: muestra en verde el interruptor de continuación activado.

`border-color`: aplica un borde negro con 15 % de opacidad.

---

```css
.edit-form .row.g-3.mb-4 .form-check.form-switch {
  display: flex;
  align-items: center;
  gap: .28rem;
  padding-left: 0;
}
```

`display: flex`: organiza el interruptor y su etiqueta en una fila.

`align-items: center`: los centra verticalmente.

`gap: .28rem`: deja `0.28rem` entre ambos.

`padding-left: 0`: elimina el espacio izquierdo aplicado por Bootstrap.

---

```css
.edit-form .row.g-3.mb-4 .form-check-input {
  margin: 0;
}
```

`margin: 0`: elimina el margen de Bootstrap alrededor del interruptor.

---

```css
.edit-form .row.g-3.mb-4 label.form-check-label[for="id_tendra_continuacion"] {
  white-space: nowrap;
  margin-left: .25rem !important;
}
```

`white-space: nowrap`: impide que la etiqueta se divida en varias líneas.

`margin-left: .25rem !important`: deja `0.25rem` a la izquierda y prevalece sobre el margen utilitario de Bootstrap.

---

```css
.input-search {
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 16 16' fill='%23cfc6ff'%3E%3Cpath d='M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001l3.85 3.85a1 1 0 0 0 1.415-1.415l-3.867-3.833zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0'/%3E%3C/svg%3E")
              no-repeat 16px 50% / 18px 18px;
  padding-left: 48px;
}
```

`background`: muestra un icono SVG de lupa de 18 píxeles, sin repetición, situado a 16 píxeles de la izquierda y centrado verticalmente.

`padding-left: 48px`: reserva espacio para que el texto no se superponga al icono.

---

```css
.edit-form input.form-control::-webkit-input-placeholder,
.input-search::-webkit-input-placeholder {
  color: rgba(246,243,255,.8);
}
```

`color`: muestra los placeholders de WebKit y Blink en blanco lavanda con 80 % de opacidad.

---

```css
.edit-form input.form-control::-moz-placeholder,
.input-search::-moz-placeholder {
  color: rgba(246,243,255,.8);
  opacity: 1;
}
```

`color`: aplica el mismo blanco lavanda a los placeholders de Firefox.

`opacity: 1`: evita que Firefox reduzca adicionalmente su opacidad.

---

```css
.edit-form input.form-control::placeholder,
.input-search::placeholder {
  color: rgba(246,243,255,.8);
}
```

`color`: aplica el blanco lavanda con 80 % de opacidad al placeholder estándar.

---

```css
.tile form .form-control {
  background-color: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.14);
  border-radius: 12px;
  color: #fff;
  padding: .6rem .8rem;
  font-size: 1rem;
  -webkit-text-fill-color: #fff;
}
```

Este bloque define la apariencia compartida de los controles de formulario contenidos en paneles `.tile`. El selector y sus valores se conservan sin limitar su alcance a una página.

---

```css
.tile form .form-control:focus {
  border-color: rgba(168,85,247,.6);
  box-shadow: 0 0 0 .2rem rgba(168,85,247,.15);
  outline: 0;
}
```

El estado enfocado conserva el borde morado translúcido, el anillo exterior y la eliminación del contorno nativo.

---

```css
.tile form .form-control::placeholder {
  color: rgba(255,255,255,.62);
  opacity: 1;
}
.tile form .form-control::-webkit-input-placeholder {
  color: rgba(255,255,255,.62);
}
```

Los placeholders de controles dentro de paneles mantienen blanco con 62 % de opacidad y la variante compatible con WebKit.

---

```css
.form-check.form-switch {
  min-width: 150px;
}
.form-check.form-switch .form-check-label {
  cursor: pointer;
  user-select: none;
}
```

Los switches conservan un ancho mínimo de 150 píxeles. Sus etiquetas muestran cursor de interacción e impiden seleccionar accidentalmente el texto.

La regla compartida de `.form-check-input` ya declara `cursor: pointer`, por lo que la declaración idéntica procedente de Search quedó consolidada sin duplicarse.

---

```css
.edit-card input[name="favorita"].form-check-input:checked {
  background-color: #ffd700;
  border-color: rgba(0,0,0,.15);
}
.edit-card input[name="volveria_a_ver"].form-check-input:checked {
  background-color: #1e90ff;
  border-color: rgba(0,0,0,.15);
}
.edit-card input[name="tendra_continuacion"].form-check-input:checked {
  background-color: #2ecc71;
  border-color: rgba(0,0,0,.15);
}
```

Las rutas por atributo `name` mantienen los colores dorado, azul y verde de los estados activados. Conviven con las rutas por ID para cubrir formularios con distintas formas de generar identificadores.

---

```css
#filtro-contenidos::-webkit-input-placeholder,
#filtro-mara::-webkit-input-placeholder {
  color: rgba(246,243,255,.8);
}
#filtro-contenidos::-moz-placeholder,
#filtro-mara::-moz-placeholder {
  color: rgba(246,243,255,.8);
  opacity: 1;
}
#filtro-contenidos::placeholder,
#filtro-mara::placeholder {
  color: rgba(246,243,255,.8);
}
```

Los filtros de Maratones conservan sus IDs, el color de placeholder con 80 % de opacidad y las variantes compatibles con WebKit y Firefox.

## css/components/custom-select.css

```css
.ct-select {
  position: relative;
  font-family: var(--font-family-interface);
}
```

`position: relative`: establece la referencia de posicionamiento para el selector nativo interno.

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz `'Teko', system-ui, sans-serif`.

---

```css
.ct-select select {
  opacity: 0;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
```

`opacity: 0`: oculta visualmente el selector nativo.

`position: absolute` e `inset: 0`: lo superponen a todo el componente.

`width` y `height: 100%`: hacen que cubra el área completa.

`pointer-events: none`: impide que reciba interacciones del puntero.

---

```css
.ct-trigger {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .6rem;
  width: 100%;
  border: 1px solid var(--color-border-subtle);
  border-radius: 14px;
  padding: .85rem .95rem;
  background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.03));
  color: var(--color-text-primary);
  font-weight: 700;
  letter-spacing: .3px;
  box-shadow: 0 10px 22px rgba(0,0,0,.25), inset 0 0 0 1px rgba(255,255,255,.05);
  transition: border-color .15s ease, box-shadow .2s ease, transform .06s ease;
  cursor: pointer;
}
```

`display: flex`: coloca el texto y el indicador en una fila.

`align-items: center`: los centra verticalmente.

`justify-content: space-between`: los separa hacia extremos opuestos.

`gap: .6rem`: mantiene `0.6rem` entre ambos.

`width: 100%`: ocupa todo el ancho disponible.

`border`: aplica el borde tenue definido por `--color-border-subtle`.

`border-radius: 14px`: redondea las esquinas.

`padding`: añade `0.85rem` vertical y `0.95rem` horizontal.

`background`: crea un degradado blanco semitransparente.

`color: var(--color-text-primary)`: aplica el blanco lavanda `#f6f3ff`.

`font-weight: 700`: muestra el texto en negrita.

`letter-spacing: .3px`: separa las letras 0.3 píxeles.

`box-shadow`: añade una sombra exterior negra y una línea blanca interior.

`transition`: suaviza los cambios de borde, sombra y posición.

`cursor: pointer`: señala que el activador es interactivo.

---

```css
.ct-trigger:hover {
  transform: translateY(-1px);
}
```

`transform`: eleva el activador un píxel al pasar el cursor.

---

```css
.ct-trigger:focus-visible {
  outline: none;
  border-color: rgba(155,92,251,.65);
  box-shadow: 0 0 0 3px rgba(155,92,251,.15), 0 12px 28px rgba(0,0,0,.35);
}
```

`outline: none`: elimina el contorno nativo visible por teclado.

`border-color`: aplica un borde morado con 65 % de opacidad.

`box-shadow`: añade un anillo morado y una sombra negra inferior.

---

```css
.ct-caret {
  width: 18px;
  height: 18px;
  flex: 0 0 18px;
  background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'><path fill='%239b5cfb' d='M5.5 7.5L10 12l4.5-4.5H5.5z'/></svg>") no-repeat center/contain;
  opacity: .9;
  transition: transform .15s ease;
}
```

`width` y `height: 18px`: fijan el tamaño del indicador.

`flex: 0 0 18px`: evita que cambie de tamaño dentro del activador.

`background`: muestra centrada una flecha SVG morada sin repetición.

`opacity: .9`: la muestra con 90 % de opacidad.

`transition`: suaviza su rotación durante 0.15 segundos.

---

```css
.ct-open .ct-caret {
  transform: rotate(180deg);
}
```

`transform`: gira el indicador 180 grados cuando el selector está abierto.

---

```css
#ct-portal {
  z-index: 9999;
}
```

`z-index: 9999`: coloca el portal de menús por encima de la mayoría de las capas de la interfaz.

---

```css
#ct-portal .ct-menu {
  background: linear-gradient(180deg, var(--color-surface-elevated, #1a1030), var(--color-surface-base, #120a1f));
  border: 1px solid rgba(155,92,251,.28);
  box-shadow: 0 14px 28px rgba(0,0,0,.55), inset 0 0 0 1px rgba(255,255,255,.05);
  border-radius: 12px;
  padding: 4px;
  font-size: .9rem;
  max-width: 260px;
}
```

`background`: crea un degradado desde `--color-surface-elevated`, actualmente `#1a1030`, hasta `--color-surface-base`, actualmente `#120a1f`.

`border`: aplica un borde morado con 28 % de opacidad.

`box-shadow`: añade una sombra negra exterior y una línea blanca interior.

`border-radius: 12px`: redondea el menú.

`padding: 4px`: deja cuatro píxeles entre su borde y las opciones.

`font-size: .9rem`: reduce el texto al 90 % del tamaño base.

`max-width: 260px`: limita el ancho a 260 píxeles.

---

```css
#ct-portal .ct-option {
  color: var(--color-text-primary, #f6f3ff);
  padding: .4rem .65rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: .95rem;
  user-select: none;
}
```

`color`: aplica `--color-text-primary`, actualmente `#f6f3ff`, con ese mismo color como respaldo.

`padding`: añade `0.4rem` vertical y `0.65rem` horizontal.

`border-radius: 8px`: redondea cada opción.

`font-weight: 600`: aplica un grosor seminegrita.

`font-size: .95rem`: reduce el texto al 95 % del tamaño base.

`user-select: none`: impide seleccionar el texto de la opción.

---

```css
#ct-portal .ct-option:hover {
  background: rgba(155,92,251,.18);
}
```

`background`: muestra un fondo morado con 18 % de opacidad al pasar el cursor.

---

```css
#ct-portal .ct-option[aria-selected="true"] {
  background: rgba(155,92,251,.28);
  box-shadow: inset 0 0 0 1px rgba(155,92,251,.4);
}
```

`background`: muestra un fondo morado con 28 % de opacidad para la opción seleccionada.

`box-shadow`: dibuja una línea morada interior con 40 % de opacidad.

---

```css
#ct-portal .ct-option.is-placeholder {
  color: var(--color-text-secondary);
}
```

`color: var(--color-text-secondary)`: aplica el lavanda secundario `#dcd3fb` a la opción placeholder.

---

```css
#ct-portal .ct-option[aria-disabled="true"] {
  opacity: .45;
  cursor: not-allowed;
}
```

`opacity: .45`: atenúa la opción deshabilitada al 45 %.

`cursor: not-allowed`: muestra que la opción no puede seleccionarse.

---

```css
#ct-portal .ct-menu::-webkit-scrollbar {
  width: 10px;
}
```

`width: 10px`: fija en diez píxeles el ancho de la barra de desplazamiento en WebKit.

---

```css
#ct-portal .ct-menu::-webkit-scrollbar-thumb {
  background: rgba(255,255,255,.18);
  border-radius: 999px;
}
```

`background`: aplica blanco con 18 % de opacidad al control de desplazamiento.

`border-radius: 999px`: redondea completamente sus extremos.

## css/components/modal.css

```css
.modal .modal-dialog .modal-content.ctmodal {
  background: linear-gradient(180deg,
              rgba(30, 20, 50, .88),
              rgba(20, 15, 30, .95));
  color: var(--color-text-primary);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 18px;
  box-shadow:
    0 24px 60px rgba(0,0,0,.65),
    0 0 0 1px rgba(255,255,255,.04) inset,
    0 0 36px rgba(155,92,251,.25);
  backdrop-filter: blur(14px) saturate(150%);
  overflow: hidden;
  animation: ctmodal-pop .28s ease-out both;
}
```

`background`: crea un degradado vertical morado oscuro y semitransparente.

`color: var(--color-text-primary)`: aplica el blanco lavanda `#f6f3ff`.

`border`: dibuja un borde blanco con 8 % de opacidad.

`border-radius: 18px`: redondea el modal.

`box-shadow`: añade una sombra negra profunda, una línea blanca interior y un resplandor morado.

`backdrop-filter`: desenfoca 14 píxeles el fondo y aumenta su saturación al 150 %.

`overflow: hidden`: recorta el contenido en las esquinas redondeadas.

`animation`: ejecuta `ctmodal-pop` durante 0.28 segundos y conserva sus estados inicial y final.

---

```css
.modal-backdrop.show {
  background:
    radial-gradient(800px 500px at 25% 25%, rgba(155,92,251,.22), transparent),
    radial-gradient(700px 420px at 70% 75%, rgba(20,255,233,.12), transparent),
    #000;
  opacity: .65;
}
```

`background`: superpone resplandores morado y cian sobre un fondo negro.

`opacity: .65`: muestra la capa completa con 65 % de opacidad.

---

```css
.ctmodal-close {
  position: absolute;
  right: 10px;
  top: 10px;
  z-index: 2;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,.5));
  opacity: .9;
}
```

`position: absolute`: permite colocar el cierre sobre el modal.

`right` y `top: 10px`: lo separan diez píxeles de los bordes superior y derecho.

`z-index: 2`: lo coloca por encima del contenido cercano.

`filter`: añade una sombra negra bajo su forma.

`opacity: .9`: lo muestra con 90 % de opacidad.

---

```css
.ctmodal-close:hover {
  opacity: 1;
}
```

`opacity: 1`: muestra el cierre completamente opaco al pasar el cursor.

---

```css
.ctmodal-header {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: 18px 18px 10px 18px;
}
```

`display: flex`: coloca el icono y el título en una fila.

`align-items: center`: los centra verticalmente.

`gap: .6rem`: deja `0.6rem` entre ambos.

`padding`: añade 18 píxeles arriba y a los lados, y diez abajo.

---

```css
.ctmodal-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: rgba(155,92,251,.18);
  box-shadow: inset 0 0 0 1px rgba(155,92,251,.35);
  color: #ffd15c;
}
```

`display: inline-flex`: mantiene el icono en línea y permite centrarlo.

`align-items` y `justify-content: center`: centran su contenido en ambos ejes.

`width` y `height: 34px`: fijan un área cuadrada.

`border-radius: 10px`: redondea sus esquinas.

`background`: aplica un fondo morado con 18 % de opacidad.

`box-shadow`: dibuja una línea morada interior con 35 % de opacidad.

`color: #ffd15c`: muestra el icono en amarillo claro.

---

```css
.ctmodal-header .ctmodal-title {
  font-family: var(--font-family-interface);
  font-weight: 900;
  letter-spacing: .3px;
}
```

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz.

`font-weight: 900`: muestra el título con el máximo grosor.

`letter-spacing: .3px`: separa sus letras 0.3 píxeles.

---

```css
.ctmodal-body {
  padding: 6px 18px 4px 18px;
  color: var(--color-text-primary);
}
```

`padding`: añade 6 píxeles arriba, 18 a los lados y 4 abajo.

`color: var(--color-text-primary)`: aplica el blanco lavanda `#f6f3ff`.

---

```css
.ctmodal-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: .6rem;
  padding: 14px 18px 18px 18px;
  background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.02));
  border-top: 1px solid rgba(255,255,255,.06);
}
```

`display: flex`: organiza las acciones en una fila.

`align-items: center`: las centra verticalmente.

`justify-content: flex-end`: las alinea a la derecha.

`gap: .6rem`: deja `0.6rem` entre acciones.

`padding`: añade 14 píxeles arriba y 18 en los demás lados.

`background`: crea un degradado blanco casi transparente.

`border-top`: separa las acciones con una línea blanca al 6 %.

---

```css
.btn-ghost-sm[data-bs-target="#confirmarEliminarModal"] {
  color: #ff4d4f;
  border: 1px solid rgba(255,77,79,.6);
  border-radius: 8px;
  padding: 4px 6px;
  line-height: 1;
  transition: all .2s ease;
}
```

`color: #ff4d4f`: muestra en rojo la acción destructiva.

`border`: aplica un borde rojo con 60 % de opacidad.

`border-radius: 8px`: redondea sus esquinas.

`padding`: añade cuatro píxeles verticales y seis horizontales.

`line-height: 1`: ajusta la altura de línea al tamaño de fuente.

`transition`: suaviza cualquier cambio durante 0.2 segundos.

---

```css
.btn-ghost-sm[data-bs-target="#confirmarEliminarModal"]:hover {
  color: #fff;
  background: rgba(255,77,79,.85);
  border-color: #ff4d4f;
  box-shadow: 0 0 12px rgba(255,77,79,.55);
}
```

`color: #fff`: cambia el contenido a blanco.

`background`: aplica rojo con 85 % de opacidad.

`border-color: #ff4d4f`: muestra el borde rojo sólido.

`box-shadow`: añade un resplandor rojo con 55 % de opacidad.

---

```css
.ctmodal .btn-outline-light {
  color: var(--color-text-primary);
  border-color: rgba(255,255,255,.22);
}
```

`color: var(--color-text-primary)`: aplica el blanco lavanda `#f6f3ff`.

`border-color`: aplica un borde blanco con 22 % de opacidad.

---

```css
.ctmodal .btn-outline-light:hover {
  background: rgba(255,255,255,.08);
  border-color: rgba(255,255,255,.3);
}
```

`background`: aplica un fondo blanco con 8 % de opacidad.

`border-color`: aumenta la opacidad del borde blanco al 30 %.

## css/components/tiles.css

```css
.tile {
  background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04));
  border: 1px solid var(--color-border-subtle);
  border-radius: 18px;
  padding: 16px;
  box-shadow: 0 14px 28px rgba(0,0,0,.35);
  backdrop-filter: blur(6px);
  animation: floatUp .5s ease both;
  transition: transform .15s ease;
}
```

`background`: crea un degradado vertical blanco semitransparente, del 8 % de opacidad arriba al 4 % abajo.

`border: 1px solid var(--color-border-subtle)`: aplica el borde tenue `rgba(255,255,255,.12)` definido por `--color-border-subtle`.

`border-radius: 18px`: redondea las esquinas del panel.

`padding: 16px`: deja 16 píxeles entre el borde y el contenido.

`box-shadow`: proyecta una sombra negra con 35 % de opacidad.

`backdrop-filter: blur(6px)`: desenfoca seis píxeles el contenido situado detrás.

`animation`: ejecuta `floatUp` durante medio segundo y conserva sus estados inicial y final.

`transition`: suaviza los cambios de transformación durante 0.15 segundos.

---

```css
.tile:hover {
  transform: translateY(-2px);
}
```

`transform: translateY(-2px)`: eleva el panel dos píxeles al pasar el cursor.

---

```css
.tile-header {
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .6px;
  color: var(--color-text-secondary);
  font-weight: 700;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: .5rem;
}
```

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz `'Teko', system-ui, sans-serif`.

`text-transform: uppercase`: muestra el encabezado en mayúsculas.

`letter-spacing: .6px`: separa las letras 0.6 píxeles.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb`.

`font-weight: 700`: muestra el encabezado en negrita.

`margin-bottom: 8px`: deja ocho píxeles debajo del encabezado.

`display: flex`: organiza sus elementos en una fila flexible.

`align-items: center`: centra verticalmente sus elementos.

`gap: .5rem`: deja medio `rem` entre ellos.

## css/components/posters.css

```css
.edit-poster {
  position: sticky;
  top: 18px;
  border-radius: 14px;
  border: 1px solid var(--color-border-subtle);
  background: #0b0b0f;
  overflow: hidden;
  box-shadow: 0 12px 28px rgba(0,0,0,.5);
}
```

`position: sticky`: mantiene el póster visible dentro de su contenedor durante el desplazamiento.

`top: 18px`: deja 18 píxeles entre el póster fijado y la parte superior.

`border-radius: 14px`: redondea sus esquinas.

`border`: dibuja un borde con `--color-border-subtle`, actualmente `rgba(255,255,255,.12)`.

`background: #0b0b0f`: aplica un fondo negro azulado.

`overflow: hidden`: recorta la imagen en las esquinas redondeadas.

`box-shadow`: proyecta una sombra negra con 50 % de opacidad.

---

```css
.edit-poster img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  aspect-ratio: 2/3;
  transform: scale(1.01);
  transition: transform .35s ease;
}
```

`width` y `height: 100%`: hacen que la imagen ocupe todo el contenedor.

`display: block`: elimina el espacio inferior propio de imágenes en línea.

`object-fit: cover`: llena el área conservando la proporción y recortando el excedente.

`aspect-ratio: 2/3`: mantiene una proporción vertical de póster.

`transform: scale(1.01)`: amplía la imagen un 1 %.

`transition`: suaviza los cambios de escala durante 0.35 segundos.

---

```css
.edit-poster:hover img {
  transform: scale(1.03);
}
```

`transform: scale(1.03)`: amplía la imagen un 3 % al pasar el cursor.

---

```css
.edit-poster-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  aspect-ratio: 2 / 3;
}
```

`display: flex`: organiza el contenido del placeholder con Flexbox.

`align-items` y `justify-content: center`: centran su contenido vertical y horizontalmente.

`aspect-ratio: 2 / 3`: conserva la proporción vertical de un póster.

---

```css
.edit-poster-placeholder i {
  font-size: 3rem;
}
```

`font-size: 3rem`: muestra el icono con un tamaño de tres veces la fuente base.

---

```css
.poster-ph {
  width: 100%;
  aspect-ratio: 2 / 3;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #aaa;
  background: rgba(255,255,255,.06);
}
```

`width: 100%`: ocupa todo el ancho disponible.

`aspect-ratio: 2 / 3`: conserva la proporción vertical de un póster.

`display: flex`: organiza el contenido mediante Flexbox.

`align-items` y `justify-content: center`: centran el contenido vertical y horizontalmente.

`color: #aaa`: aplica gris claro al icono o texto del placeholder.

`background`: aplica un fondo blanco con 6 % de opacidad.

---

```css
.plat-ph {
  width: 100%;
  height: 100%;
  display: grid;
  place-items: center;
  color: var(--color-text-secondary);
  background: rgba(255,255,255,.06);
}
```

`width` y `height: 100%`: hacen que el placeholder ocupe todo su contenedor.

`display: grid`: organiza el contenido mediante Grid.

`place-items: center`: centra el contenido en ambos ejes.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb`.

`background`: aplica un fondo blanco con 6 % de opacidad.

---

```css
.kan-poster {
  color: inherit;
  text-decoration: none;
}
```

`color: inherit`: utiliza el color heredado del contenedor.

`text-decoration: none`: elimina el subrayado cuando el póster es un enlace.

---

```css
.kan-poster:hover {
  color: #fff;
}
```

`color: #fff`: muestra en blanco el contenido del enlace al pasar el cursor.

---

```css
.kan-poster img {
  width: 100%;
  aspect-ratio: 2/3;
  object-fit: cover;
  display: block;
  transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
  box-shadow: 0 8px 22px rgba(10,0,40,.28);
  filter: saturate(1.02);
}
```

`width: 100%`: ocupa todo el ancho del contenedor.

`aspect-ratio: 2/3`: conserva la proporción de póster.

`object-fit: cover`: llena el área conservando la proporción y recortando el excedente.

`display: block`: elimina el espacio inferior propio de imágenes en línea.

`transition`: suaviza durante 0.15 segundos los cambios de posición, sombra y filtro.

`box-shadow`: proyecta una sombra morada oscura con 28 % de opacidad.

`filter: saturate(1.02)`: aumenta la saturación de la imagen un 2 %.

---

```css
.rail-poster {
  color: inherit;
  text-decoration: none;
}
```

`color: inherit`: utiliza el color heredado del contenedor.

`text-decoration: none`: elimina el subrayado del enlace.

---

```css
.rail-poster:hover {
  color: #fff;
}
```

`color: #fff`: muestra en blanco el contenido al pasar el cursor.

---

```css
.rail-poster img {
  width: 100%;
  aspect-ratio: 2/3;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  box-shadow: 0 8px 22px rgba(10,0,40,.3);
  transition: transform .16s ease, box-shadow .16s ease;
}
```

`width: 100%`: ocupa todo el ancho disponible.

`aspect-ratio: 2/3`: conserva la proporción vertical.

`object-fit: cover`: llena el área sin deformar la imagen.

`display: block`: elimina el espacio inferior de imágenes en línea.

`border-radius: 14px`: redondea las esquinas.

`box-shadow`: añade una sombra morada oscura con 30 % de opacidad.

`transition`: suaviza durante 0.16 segundos los cambios de posición y sombra.

---

```css
.kan-poster .poster-ph {
  transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
  box-shadow: 0 8px 22px rgba(10,0,40,.28);
  filter: saturate(1.02);
}
```

`transition`: suaviza los cambios de posición, sombra y filtro del placeholder durante 0.15 segundos.

`box-shadow`: aplica la misma sombra oscura que al póster Kanban real.

`filter: saturate(1.02)`: aumenta la saturación un 2 %.

---

```css
.rail-poster .poster-ph {
  display: block;
  border-radius: 14px;
  box-shadow: 0 8px 22px rgba(10,0,40,.3);
  transition: transform .16s ease, box-shadow .16s ease;
  filter: saturate(1.02);
}
```

`display: block`: hace que el placeholder se comporte como bloque dentro del enlace.

`border-radius: 14px`: redondea sus esquinas.

`box-shadow`: aplica la misma sombra que al póster real del rail.

`transition`: suaviza los cambios de posición y sombra durante 0.16 segundos.

`filter: saturate(1.02)`: aumenta la saturación un 2 %.

---

```css
.rail-poster:hover img {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(10,0,40,.36);
}
```

`transform: translateY(-2px)`: eleva la imagen dos píxeles al pasar el cursor.

`box-shadow`: amplía la sombra y aumenta su opacidad al 36 %.

---

```css
.catalog-card-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  aspect-ratio: 2 / 3;
}
```

`display: flex`: organiza el contenido mediante Flexbox.

`align-items` y `justify-content: center`: centran el contenido en ambos ejes.

`height: 100%`: ocupa toda la altura disponible.

`aspect-ratio: 2 / 3`: conserva la proporción vertical de póster.

---

```css
.catalog-card-placeholder i {
  font-size: 1.6rem;
}
```

`font-size: 1.6rem`: muestra el icono al 160 % del tamaño base.

## css/components/rails.css

```css
.rail-track {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: minmax(140px, 170px);
  gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding-bottom: .25rem;
}
```

`display: grid`: organiza el carril como una cuadrícula.

`grid-auto-flow: column`: crea nuevas celdas horizontalmente.

`grid-auto-columns: minmax(140px, 170px)`: limita cada columna automática a un ancho de entre 140 y 170 píxeles.

`gap: 1rem`: separa las tarjetas del carril.

`overflow-x: auto`: permite desplazamiento horizontal cuando el contenido excede el ancho disponible.

`scroll-snap-type: x mandatory`: activa el ajuste obligatorio de desplazamiento sobre el eje horizontal.

`padding-bottom: .25rem`: reserva espacio inferior dentro del carril.

---

```css
.rail-track::-webkit-scrollbar {
  height: 0;
}
```

`height: 0`: oculta visualmente el scrollbar horizontal en motores WebKit sin desactivar el desplazamiento.

---

```css
.rail-card {
  position: relative;
  scroll-snap-align: start;
}
```

`position: relative`: establece la tarjeta como referencia de posicionamiento para elementos superpuestos.

`scroll-snap-align: start`: alinea el inicio de la tarjeta con el inicio visible del carril durante el ajuste de desplazamiento.

## css/components/audiovisual-cards.css

```css
.topcard {
  display: flex;
  flex-direction: column;
  height: 100%;
}
```

`display: flex`: organiza la tarjeta mediante Flexbox.

`flex-direction: column`: coloca sus secciones una debajo de otra.

`height: 100%`: ocupa toda la altura disponible.

---

```css
.topcard-thumb {
  position: relative;
  width: 100%;
  aspect-ratio: 2 / 3;
  overflow: hidden;
  flex: 0 0 auto;
  border-radius: inherit;
  color: inherit;
  text-decoration: none;
}
```

`position: relative`: establece la miniatura como referencia para elementos posicionados dentro de ella.

`width: 100%`: ocupa todo el ancho de la tarjeta.

`aspect-ratio: 2 / 3`: conserva la proporción de póster.

`overflow: hidden`: recorta el contenido que sobresale.

`flex: 0 0 auto`: evita que la miniatura crezca o se reduzca.

`border-radius: inherit`: hereda el redondeo del contenedor.

`color: inherit`: utiliza el color heredado.

`text-decoration: none`: elimina el subrayado si es un enlace.

---

```css
.topcard-thumb:hover {
  color: #fff;
}
```

`color: #fff`: muestra en blanco el contenido al pasar el cursor.

---

```css
.topcard-thumb > a {
  color: inherit;
  text-decoration: none;
}
```

`color: inherit`: hace que el enlace directo use el color de la miniatura.

`text-decoration: none`: elimina su subrayado.

---

```css
.topcard-thumb > a:hover {
  color: #fff;
}
```

`color: #fff`: muestra el enlace directo en blanco al pasar el cursor.

---

```css
.topcard-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```

`width` y `height: 100%`: hacen que la imagen llene la miniatura.

`object-fit: cover`: mantiene la proporción y recorta el excedente.

`display: block`: elimina el espacio inferior de imágenes en línea.

---

```css
.topcard-meta {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}
```

`flex: 1 1 auto`: permite que el área de metadatos crezca y se reduzca según el espacio.

`display: flex`: organiza su contenido con Flexbox.

`flex-direction: column`: coloca los metadatos verticalmente.

---

```css
.topcard .topcard-meta > .d-flex.align-items-center.justify-content-between {
  margin-top: auto;
}
```

`margin-top: auto`: empuja la fila de acciones hacia la parte inferior de la tarjeta.

---

```css
.topcard-name {
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.3;
  min-height: 2.6em;
  max-height: 2.6em;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
}
```

`font-size: 0.95rem`: reduce el texto al 95 % del tamaño base.

`font-weight: 600`: aplica un grosor seminegrita.

`line-height: 1.3`: establece una altura de línea de 1.3 veces la fuente.

`min-height` y `max-height: 2.6em`: reservan exactamente el espacio de dos líneas.

`overflow: hidden`: oculta el texto que excede esa altura.

`display: -webkit-box`: habilita el recorte multilínea compatible con WebKit.

`-webkit-line-clamp: 2`: limita el título a dos líneas.

`-webkit-box-orient: vertical`: organiza esas líneas verticalmente.

`text-overflow: ellipsis`: indica el desbordamiento con puntos suspensivos cuando el navegador lo admite.

---

```css
.topcard-name a {
  color: inherit;
  text-decoration: none;
}
```

`color: inherit`: hace que el enlace use el color del título.

`text-decoration: none`: elimina el subrayado.

---

```css
.topcard-name a:hover {
  color: #fff;
}
```

`color: #fff`: muestra el título en blanco al pasar el cursor.

## css/components/pagination.css

```css
.pagination {
  display: flex;
  gap: 6px;
  justify-content: center;
  margin-top: 20px;
}
```

`display: flex`: organiza los elementos de paginación en una fila flexible.

`gap: 6px`: deja seis píxeles entre cada elemento.

`justify-content: center`: centra horizontalmente la paginación.

`margin-top: 20px`: separa la paginación 20 píxeles del contenido anterior.

---

```css
.page-item .page-link {
  border-radius: 10px;
  border: 1px solid var(--color-border-subtle);
  background: rgba(255,255,255,.05);
  color: var(--color-text-secondary);
  text-decoration: none;
  font-family: var(--font-family-interface);
  font-weight: 700;
  padding: .55rem .9rem;
  transition: all .15s ease;
}
```

`border-radius: 10px`: redondea las esquinas del enlace.

`border: 1px solid var(--color-border-subtle)`: aplica el borde tenue `rgba(255,255,255,.12)`.

`background`: usa un fondo blanco con 5 % de opacidad.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb`.

`text-decoration: none`: elimina el subrayado del enlace.

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz `'Teko', system-ui, sans-serif`.

`font-weight: 700`: muestra el texto en negrita.

`padding`: añade `0.55rem` vertical y `0.9rem` horizontal.

`transition`: suaviza cualquier cambio durante 0.15 segundos.

---

```css
.page-item .page-link:hover {
  color: #fff;
  background: linear-gradient(135deg, var(--accent), var(--color-accent-dark));
  box-shadow: 0 0 12px rgba(155,92,251,.5);
  border-color: transparent;
}
```

`color: #fff`: muestra el texto en blanco al pasar el cursor.

`background`: aplica un degradado diagonal desde `--accent` (`#9b5cfb`) hasta `--color-accent-dark` (`#6f3fe6`).

`box-shadow`: añade un resplandor morado con 50 % de opacidad.

`border-color: transparent`: oculta el color del borde.

---

```css
.page-item.active .page-link,
.page-item .page-link:focus {
  color: #fff;
  background: linear-gradient(135deg, var(--accent), var(--color-accent-dark));
  border-color: transparent;
  box-shadow: 0 0 14px rgba(111,63,230,.6);
}
```

`color: #fff`: muestra en blanco el enlace activo o enfocado.

`background`: aplica el degradado morado de los colores de acento.

`border-color: transparent`: oculta el color del borde.

`box-shadow`: añade un resplandor morado oscuro con 60 % de opacidad.

---

```css
.page-item.disabled .page-link {
  color: #777;
  background: rgba(255,255,255,.04);
  border-color: var(--color-border-subtle);
  opacity: .6;
}
```

`color: #777`: muestra el texto en gris medio.

`background`: aplica un fondo blanco con 4 % de opacidad.

`border-color: var(--color-border-subtle)`: conserva el borde tenue definido por `--color-border-subtle`.

`opacity: .6`: atenúa el enlace deshabilitado al 60 %.

## css/components/podium.css

---

```css
.podium-stage {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: end;
  gap: 1rem;
  min-height: 360px;
}
```

`display: grid`: organiza el podio mediante Grid.

`grid-template-columns: 1fr 1fr 1fr`: crea tres columnas del mismo ancho.

`align-items: end`: alinea las posiciones con la parte inferior de sus áreas.

`gap: 1rem`: deja un `rem` entre columnas.

`min-height: 360px`: reserva al menos 360 píxeles de altura.

---

```css
.podium-slot {
  text-align: center;
  position: relative;
  transition: transform .4s ease, filter .3s ease;
}
```

`text-align: center`: centra el contenido textual.

`position: relative`: establece la posición como referencia para su pedestal absoluto.

`transition`: suaviza los cambios de transformación durante 0.4 segundos y de filtro durante 0.3.

---

```css
.podium-poster {
  color: inherit;
  text-decoration: none;
}
```

`color: inherit`: utiliza el color heredado del contenedor.

`text-decoration: none`: elimina el subrayado si el póster es un enlace.

---

```css
.podium-poster:hover {
  color: #fff;
}
```

`color: #fff`: muestra en blanco el contenido al pasar el cursor.

---

```css
.podium-slot .podium-poster img {
  width: 100%;
  max-width: 200px;
  aspect-ratio: 2/3;
  object-fit: cover;
  border-radius: 14px;
  box-shadow: 0 12px 30px rgba(10,0,40,.4);
  margin-inline: auto;
  display: block;
}
```

`width: 100%`: permite que la imagen ocupe el ancho disponible.

`max-width: 200px`: limita su ancho a 200 píxeles.

`aspect-ratio: 2/3`: conserva la proporción vertical de póster.

`object-fit: cover`: llena el área sin deformar la imagen.

`border-radius: 14px`: redondea las esquinas.

`box-shadow`: proyecta una sombra morada oscura con 40 % de opacidad.

`margin-inline: auto`: centra horizontalmente la imagen.

`display: block`: elimina el espacio inferior de imágenes en línea.

---

```css
.podium-slot .poster-ph {
  max-width: 200px;
  display: block;
  border-radius: 14px;
  box-shadow: 0 12px 30px rgba(10,0,40,.4);
  margin-inline: auto;
  transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
  filter: saturate(1.02);
}
```

`max-width: 200px`: limita el placeholder al mismo ancho que el póster.

`display: block`: lo hace comportarse como bloque.

`border-radius: 14px`: redondea sus esquinas.

`box-shadow`: aplica la misma sombra oscura del póster.

`margin-inline: auto`: lo centra horizontalmente.

`transition`: suaviza cambios de posición, sombra y filtro durante 0.15 segundos.

`filter: saturate(1.02)`: aumenta la saturación un 2 %.

---

```css
.podium-label {
  margin-top: .6rem;
}
```

`margin-top: .6rem`: separa la etiqueta del póster por `0.6rem`.

---

```css
.podium-title {
  font-family: var(--brand-font);
  font-size: 1rem;
  letter-spacing: .3px;
  margin-bottom: .3rem;
  color: var(--color-text-primary);
}
```

`font-family: var(--brand-font)`: aplica la tipografía de marca `'Bebas Neue', sans-serif`.

`font-size: 1rem`: usa el tamaño base de fuente.

`letter-spacing: .3px`: separa las letras 0.3 píxeles.

`margin-bottom: .3rem`: deja `0.3rem` debajo del título.

`color: var(--color-text-primary)`: aplica el blanco lavanda `#f6f3ff`.

---

```css
.podium-slot .podium-poster img {
  outline: 4px solid transparent;
  outline-offset: -4px;
  transition: outline-color .25s ease;
}
```

`outline: 4px solid transparent`: reserva un contorno transparente de cuatro píxeles.

`outline-offset: -4px`: desplaza el contorno hacia dentro de la imagen.

`transition`: suaviza el cambio de color del contorno durante 0.25 segundos.

---

```css
.podium-slot[data-rank="1"]:hover .podium-poster img {
  outline-color: #ffd700;
}
```

`outline-color: #ffd700`: muestra un contorno dorado al pasar el cursor por el primer lugar.

---

```css
.podium-slot:has(.pedestal-2:hover) .podium-poster img {
  outline-color: #c0c0c0;
}
```

`outline-color: #c0c0c0`: muestra un contorno plateado cuando el cursor está sobre el pedestal del segundo lugar.

---

```css
.podium-slot:has(.pedestal-3:hover) .podium-poster img {
  outline-color: #cd7f32;
}
```

`outline-color: #cd7f32`: muestra un contorno bronce cuando el cursor está sobre el pedestal del tercer lugar.

---

```css
.pedestal {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 85%;
  height: 70px;
  border-radius: 10px 10px 0 0;
  background: gold;
  background: linear-gradient(180deg, #ffd700, #e6b800);
  box-shadow: 0 10px 20px rgba(0,0,0,.35);
  display: flex;
  justify-content: center;
  align-items: flex-start;
  font-family: var(--brand-font);
  font-size: 1.2rem;
}
```

`position: absolute`: saca el pedestal del flujo y permite colocarlo dentro de `.podium-slot`.

`bottom: 0`: lo fija a la parte inferior de la posición.

`left: 50%` y `transform: translateX(-50%)`: lo centran horizontalmente.

`width: 85%`: ocupa el 85 % del ancho de la posición.

`height: 70px`: fija su altura en 70 píxeles.

`border-radius`: redondea solo las esquinas superiores.

`background: gold`: proporciona un fondo dorado de respaldo.

`background: linear-gradient(...)`: sustituye el respaldo por un degradado dorado vertical cuando es compatible.

`box-shadow`: proyecta una sombra negra con 35 % de opacidad.

`display: flex`: organiza su contenido mediante Flexbox.

`justify-content: center`: centra el contenido horizontalmente.

`align-items: flex-start`: lo alinea con la parte superior.

`font-family: var(--brand-font)`: aplica la tipografía de marca.

`font-size: 1.2rem`: muestra el contenido al 120 % del tamaño base.

---

```css
.pedestal .medal {
  font-size: 1.4rem;
  font-weight: 800;
  margin-top: .4rem;
  color: #fff;
  text-shadow: 0 2px 6px rgba(0,0,0,.5);
}
```

`font-size: 1.4rem`: muestra la medalla al 140 % del tamaño base.

`font-weight: 800`: aplica un grosor intenso.

`margin-top: .4rem`: la separa de la parte superior.

`color: #fff`: muestra el contenido en blanco.

`text-shadow`: añade una sombra negra al texto con 50 % de opacidad.

---

```css
.pedestal-1 {
  z-index: 2;
}
```

`z-index: 2`: coloca el pedestal del primer lugar por encima de elementos con niveles menores.

---

```css
.pedestal-2 {
  background: linear-gradient(180deg, #c0c0c0, #a0a0a0);
}
```

`background`: aplica un degradado vertical plateado al segundo lugar.

---

```css
.pedestal-3 {
  background: linear-gradient(180deg, #cd7f32, #a0522d);
}
```

`background`: aplica un degradado vertical bronce al tercer lugar.
