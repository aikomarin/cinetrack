## css/layout/cinedock.css

```css
.cinedock-wrapper {
  position: relative;
  top: auto;
  z-index: 50;
  padding: 14px var(--film-rail-content-offset) 10px;
}
```

`position: relative`: mantiene el contenedor en el flujo normal y permite aplicar `z-index`.

`top: auto`: deja la posición vertical en su valor automático, sin desplazar el contenedor.

`z-index: 50`: coloca el contenedor por encima de elementos con niveles de apilamiento menores.

`padding: 14px var(--film-rail-content-offset) 10px`: añade 14 píxeles arriba, 10 abajo y un espacio lateral calculado con `--film-rail-content-offset`. Actualmente `--film-rail-content-offset` vale `calc(var(--film-rail-width) + 18px)` y `--film-rail-width` vale `140px`, por lo que el espacio lateral base equivale a 158 píxeles.

---

```css
.cinedock {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  background: linear-gradient(180deg, rgba(15,10,24,.85), rgba(15,10,24,.72));
  border: 1px solid var(--color-border-subtle);
  border-radius: 18px;
  padding: 10px 14px;
  backdrop-filter: blur(8px) saturate(140%);
  box-shadow: 0 10px 26px rgba(0,0,0,.45), inset 0 0 0 1px rgba(255,255,255,.06);
}
```

`display: flex`: coloca los elementos internos en una fila flexible.

`align-items: center`: centra verticalmente los elementos de la navegación.

`justify-content: space-between`: distribuye el espacio libre entre la marca, las pestañas y las acciones.

`gap: 14px`: deja 14 píxeles de separación entre los elementos directos.

`background`: crea un degradado vertical oscuro y semitransparente, más opaco arriba que abajo.

`border: 1px solid var(--color-border-subtle)`: dibuja un borde de un píxel con `--color-border-subtle`, cuyo valor actual es `rgba(255,255,255,.12)`, un blanco con 12 % de opacidad.

`border-radius: 18px`: redondea las esquinas del contenedor.

`padding: 10px 14px`: añade 10 píxeles de espacio interno vertical y 14 horizontal.

`backdrop-filter`: desenfoca 8 píxeles el contenido situado detrás y aumenta su saturación al 140 %.

`box-shadow`: añade una sombra exterior oscura y una línea interior blanca tenue.

---

```css
.dock-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 10px;
  border-radius: 12px;
  color: inherit;
  text-decoration: none;
}
```

`display: flex`: coloca el logo y el texto de marca en una fila.

`align-items: center`: centra verticalmente el logo y el texto.

`gap: 10px`: separa el logo y el texto por 10 píxeles.

`padding: 6px 10px`: añade 6 píxeles de espacio vertical y 10 horizontal.

`border-radius: 12px`: redondea el área interactiva de la marca.

`color: inherit`: usa el color de texto heredado del contenedor.

`text-decoration: none`: elimina el subrayado propio de los enlaces.

---

```css
.dock-brand:hover {
  background: rgba(255,255,255,.06);
  color: #fff;
}
```

`background`: muestra un fondo blanco con 6 % de opacidad al pasar el cursor.

`color: #fff`: cambia el contenido de la marca a blanco.

---

```css
.brand-text {
  font-family: var(--brand-font);
  letter-spacing: .8px;
  font-size: clamp(1.6rem, 2.2vw, 2.2rem);
}
```

`font-family: var(--brand-font)`: aplica la tipografía de marca. Actualmente `--brand-font` contiene `'Bebas Neue', sans-serif`.

`letter-spacing: .8px`: separa las letras por 0.8 píxeles.

`font-size`: adapta el tamaño entre `1.6rem` y `2.2rem`, usando `2.2vw` mientras se encuentre dentro de esos límites.

---

```css
.dock-tabs {
  position: relative;
  display: flex;
  align-items: center;
  gap: 6px;
}
```

`position: relative`: establece una referencia de posicionamiento para elementos internos posicionados.

`display: flex`: coloca las pestañas en una fila.

`align-items: center`: centra verticalmente las pestañas.

`gap: 6px`: separa cada pestaña por 6 píxeles.

---

```css
.dock-tab {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .5px;
  padding: 8px 12px;
  border-radius: 12px;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color .15s ease, transform .15s ease, background .15s ease;
  position: relative;
}
```

`display: flex`: coloca el icono y el texto de la pestaña en una fila.

`align-items: center`: centra verticalmente el icono y el texto.

`gap: 8px`: separa el icono y el texto por 8 píxeles.

`font-family: var(--font-family-interface)`: usa la tipografía de interfaz. Actualmente `--font-family-interface` contiene `'Teko', system-ui, sans-serif`.

`text-transform: uppercase`: muestra el texto en mayúsculas.

`letter-spacing: .5px`: separa las letras por medio píxel.

`padding: 8px 12px`: añade 8 píxeles de espacio vertical y 12 horizontal.

`border-radius: 12px`: redondea el fondo de la pestaña.

`color: var(--color-text-secondary)`: aplica el color secundario del texto. Actualmente `--color-text-secondary` contiene `#dcd3fb`, un lavanda claro.

`text-decoration: none`: elimina el subrayado del enlace.

`transition`: suaviza durante 0.15 segundos los cambios de color, posición y fondo.

`position: relative`: permite posicionar el indicador `::after` respecto a la pestaña.

---

```css
.dock-tab:hover {
  color: #fff;
  transform: translateY(-1px);
  background: rgba(255,255,255,.06);
}
```

`color: #fff`: muestra el texto y el icono en blanco al pasar el cursor.

`transform: translateY(-1px)`: eleva la pestaña un píxel.

`background`: muestra un fondo blanco con 6 % de opacidad.

---

```css
.dock-tab[aria-current="page"] {
  color: #fff;
  font-weight: 600;
}
```

`color: #fff`: muestra en blanco la pestaña que representa la página actual.

`font-weight: 600`: aumenta el grosor del texto de la pestaña activa.

---

```css
.dock-tab i {
  font-size: 1.05rem;
  opacity: .95;
}
```

`font-size: 1.05rem`: hace que el icono sea ligeramente mayor que el tamaño base del texto.

`opacity: .95`: reduce levemente la opacidad del icono.

---

```css
.dock-tab::after {
  content: "";
  position: absolute;
  bottom: -6px;
  left: 25%;
  width: 50%;
  height: 3px;
  border-radius: 6px;
  background: linear-gradient(90deg, var(--accent), var(--color-accent-dark));
  box-shadow: 0 0 6px rgba(155,92,251,.55);
  transform: scaleX(0);
  transition: transform .25s ease;
}
```

`content: ""`: crea un pseudoelemento vacío para dibujar el indicador.

`position: absolute`: permite ubicar el indicador respecto a `.dock-tab`.

`bottom: -6px`: sitúa el indicador 6 píxeles debajo de la pestaña.

`left: 25%`: comienza el indicador a una cuarta parte del ancho de la pestaña.

`width: 50%`: limita el indicador a la mitad del ancho de la pestaña.

`height: 3px`: establece una línea de 3 píxeles de alto.

`border-radius: 6px`: redondea los extremos de la línea.

`background`: crea un degradado horizontal desde `--accent`, actualmente `#9b5cfb`, hasta `--color-accent-dark`, actualmente `#6f3fe6`; ambos son tonos morados de acento.

`box-shadow`: añade un resplandor morado con 55 % de opacidad.

`transform: scaleX(0)`: oculta inicialmente la línea reduciendo su escala horizontal a cero.

`transition`: anima el cambio de escala durante 0.25 segundos.

---

```css
.dock-tab:hover::after {
  transform: scaleX(1);
}
```

`transform: scaleX(1)`: extiende el indicador hasta su ancho completo al pasar el cursor por la pestaña.

---

```css
.dock-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
```

`display: flex`: coloca las acciones en una fila.

`align-items: center`: centra verticalmente las acciones.

`gap: 8px`: separa cada acción por 8 píxeles.

---

```css
.dock-search {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  border: 1px solid var(--color-border-subtle);
  background: rgba(255,255,255,.04);
  color: inherit;
  text-decoration: none;
  transition: all .15s ease;
}
```

`display: inline-flex`: permite que la acción conserve un comportamiento en línea y centre su contenido mediante Flexbox.

`align-items: center`: centra verticalmente el icono.

`justify-content: center`: centra horizontalmente el icono.

`width: 40px`: fija el ancho en 40 píxeles.

`height: 40px`: fija la altura en 40 píxeles.

`border-radius: 10px`: redondea las esquinas.

`border: 1px solid var(--color-border-subtle)`: aplica el borde blanco tenue definido por `--color-border-subtle`, cuyo valor es `rgba(255,255,255,.12)`.

`background`: aplica un fondo blanco con 4 % de opacidad.

`color: inherit`: usa el color heredado para el icono o texto.

`text-decoration: none`: elimina el subrayado si la acción es un enlace.

`transition`: suaviza durante 0.15 segundos cualquier propiedad que cambie de valor.

---

```css
.dock-search:hover {
  background: rgba(255,255,255,.08);
  color: #fff;
}
```

`background`: aumenta el fondo blanco del 4 % al 8 % de opacidad.

`color: #fff`: muestra el icono o texto en blanco.

---

```css
.btn-appcentral-ghost {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding: .55rem .85rem;
  border-radius: 10px;
  border: 1px solid var(--color-border-subtle);
  background: rgba(255,255,255,.04);
  color: var(--color-text-secondary);
  text-decoration: none;
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .5px;
  font-weight: 600;
  transition: all .15s ease;
}
```

`display: inline-flex`: mantiene el enlace en línea y organiza su contenido con Flexbox.

`align-items: center`: centra verticalmente su icono y texto.

`gap: .5rem`: separa el icono y el texto por medio `rem`.

`padding: .55rem .85rem`: añade espacio interno vertical de `0.55rem` y horizontal de `0.85rem`.

`border-radius: 10px`: redondea las esquinas.

`border: 1px solid var(--color-border-subtle)`: usa el borde blanco tenue `rgba(255,255,255,.12)` definido por `--color-border-subtle`.

`background`: aplica un fondo blanco con 4 % de opacidad.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb` definido por `--color-text-secondary`.

`text-decoration: none`: elimina el subrayado del enlace.

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz `'Teko', system-ui, sans-serif`.

`text-transform: uppercase`: muestra el texto en mayúsculas.

`letter-spacing: .5px`: separa las letras por medio píxel.

`font-weight: 600`: aplica un grosor seminegrita.

`transition`: suaviza durante 0.15 segundos cualquier propiedad que cambie.

---

```css
.btn-appcentral-ghost i {
  opacity: .95;
}
```

`opacity: .95`: reduce ligeramente la opacidad del icono contenido en el enlace.

---

```css
.btn-appcentral-ghost:hover {
  background: rgba(255,255,255,.08);
  color: #fff;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.08);
}
```

`background`: aumenta el fondo blanco al 8 % de opacidad al pasar el cursor.

`color: #fff`: cambia el texto y el icono a blanco.

`box-shadow`: dibuja una línea blanca interior con 8 % de opacidad.

---

```css
.logo-claqueta-anim {
  position: relative;
  width: 34px;
  height: 26px;
  border-radius: 4px;
  background: linear-gradient(180deg, var(--clapboard-body-color-start), var(--clapboard-body-color-end));
  box-shadow: inset 0 0 0 2px var(--clapboard-edge-color), 0 4px 10px rgba(0,0,0,.35);
  display: inline-block;
  margin-right: .5rem;
}
```

`position: relative`: establece el cuerpo como referencia para posicionar su bisagra y su tapa.

`width: 34px`: fija el ancho del cuerpo en 34 píxeles.

`height: 26px`: fija la altura del cuerpo en 26 píxeles.

`border-radius: 4px`: redondea ligeramente las esquinas.

`background`: aplica un degradado vertical desde `--clapboard-body-color-start`, actualmente `#7c3aed`, hasta `--clapboard-body-color-end`, actualmente `#5b2bb5`; representan el morado principal y el morado oscuro del cuerpo de la claqueta.

`box-shadow`: dibuja un borde interior con `--clapboard-edge-color`, actualmente `rgba(0,0,0,.28)`, y una sombra exterior oscura.

`display: inline-block`: permite que el logo permanezca en línea y respete sus dimensiones.

`margin-right: .5rem`: separa el logo del contenido situado a su derecha.

---

```css
.logo-claqueta-anim::after {
  content: "";
  position: absolute;
  left: -3px;
  top: -4px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ddd;
  box-shadow: 0 0 0 2px var(--clapboard-edge-color);
}
```

`content: ""`: crea un pseudoelemento vacío para representar la bisagra.

`position: absolute`: permite ubicar la bisagra respecto al cuerpo del logo.

`left: -3px`: desplaza la bisagra 3 píxeles hacia la izquierda del cuerpo.

`top: -4px`: desplaza la bisagra 4 píxeles por encima del cuerpo.

`width: 8px`: fija el ancho de la bisagra.

`height: 8px`: fija la altura de la bisagra.

`border-radius: 50%`: convierte la bisagra en un círculo.

`background: #ddd`: aplica un gris claro a la superficie de la bisagra.

`box-shadow`: dibuja un contorno de 2 píxeles con `--clapboard-edge-color`, cuyo valor es `rgba(0,0,0,.28)`.

---

```css
.logo-claqueta-anim::before {
  content: "";
  position: absolute;
  left: -1px;
  top: -9px;
  width: 36px;
  height: 10px;
  border-radius: 3px;
  background: repeating-linear-gradient(45deg, var(--clapboard-stripe-color) 0 7px, #6b21a8 7px 14px);
  box-shadow: inset 0 0 0 1px var(--clapboard-edge-color), 0 2px 6px rgba(0,0,0,.35);
  filter: drop-shadow(0 2px 4px rgba(0,0,0,.35));
  transform-origin: 6px 10px;
  animation: clapOpen 2.2s ease-in-out infinite;
}
```

`content: ""`: crea un pseudoelemento vacío para dibujar la tapa.

`position: absolute`: permite ubicar la tapa respecto al cuerpo del logo.

`left: -1px`: desplaza la tapa un píxel hacia la izquierda.

`top: -9px`: coloca la tapa 9 píxeles por encima del cuerpo.

`width: 36px`: hace que la tapa mida 36 píxeles de ancho.

`height: 10px`: fija la altura de la tapa en 10 píxeles.

`border-radius: 3px`: redondea ligeramente sus esquinas.

`background`: crea franjas diagonales alternas entre `--clapboard-stripe-color`, actualmente `#fff`, y el morado oscuro `#6b21a8`.

`box-shadow`: dibuja un borde interior con `--clapboard-edge-color`, cuyo valor es `rgba(0,0,0,.28)`, y una sombra exterior.

`filter`: añade otra sombra bajo la forma completa de la tapa.

`transform-origin: 6px 10px`: sitúa el punto de giro a 6 píxeles del borde izquierdo y 10 píxeles del borde superior.

`animation`: ejecuta continuamente la animación `clapOpen`, con una duración de 2.2 segundos y aceleración suave al inicio y al final.

```css
.logo-claqueta-anim:hover::before {
  animation-play-state: paused;
}
```

`animation-play-state: paused`: detiene temporalmente la animación de la tapa mientras el cursor permanece sobre el logo.

## css/layout/clapboard.css

```css
.clap-sep {
  position: relative;
  height: 68px;
  margin: 44px 0 28px;
  display: grid;
  place-items: center;
}
```

`position: relative`: establece el separador como referencia para posicionar el cuerpo y la tapa de la claqueta.

`height: 68px`: reserva 68 píxeles de altura para el separador.

`margin: 44px 0 28px`: deja 44 píxeles de espacio arriba, ninguno a los lados y 28 abajo.

`display: grid`: convierte el separador en una cuadrícula.

`place-items: center`: centra horizontal y verticalmente el contenido de la cuadrícula.

---

```css
.clap-sep::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 76px;
  height: 34px;
  transform: translate(-50%, -2px);
  border-radius: 6px;
  background: linear-gradient(180deg, var(--clapboard-body-color-start, #7c3aed), var(--clapboard-body-color-end, #5b2bb5));
  box-shadow: inset 0 0 0 2px rgba(0,0,0,.28), 0 6px 16px rgba(0,0,0,.35);
}
```

`content: ""`: crea un pseudoelemento vacío para dibujar el cuerpo.

`position: absolute`: permite ubicar el cuerpo respecto a `.clap-sep`.

`left: 50%`: coloca el borde izquierdo en el centro horizontal del separador.

`top: 50%`: coloca el borde superior en el centro vertical del separador.

`width: 76px`: fija el ancho del cuerpo en 76 píxeles.

`height: 34px`: fija la altura del cuerpo en 34 píxeles.

`transform: translate(-50%, -2px)`: centra horizontalmente el cuerpo respecto a su propio ancho y lo eleva 2 píxeles.

`border-radius: 6px`: redondea las esquinas del cuerpo.

`background`: crea un degradado desde `--clapboard-body-color-start`, actualmente `#7c3aed`, hasta `--clapboard-body-color-end`, actualmente `#5b2bb5`. Si las variables no estuvieran definidas, usaría esos mismos valores como respaldo.

`box-shadow`: dibuja un borde interior negro con 28 % de opacidad y una sombra exterior negra con 35 % de opacidad.

---

```css
.clap-sep::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 90px;
  height: 16px;
  transform-origin: calc(-38px) 16px;
  transform: translate(-50%, -26px) rotate(0deg);
  border-radius: 4px;
  background: repeating-linear-gradient(45deg, #fff 0 8px, #6b21a8 8px 16px);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.28), 0 4px 10px rgba(0,0,0,.35);
  animation: clapOpenSep 2.3s ease-in-out infinite;
}
```

`content: ""`: crea un pseudoelemento vacío para dibujar la tapa.

`position: absolute`: permite ubicar la tapa respecto a `.clap-sep`.

`left: 50%`: coloca el borde izquierdo en el centro horizontal del separador.

`top: 50%`: coloca el borde superior en el centro vertical del separador.

`width: 90px`: fija el ancho de la tapa en 90 píxeles.

`height: 16px`: fija la altura de la tapa en 16 píxeles.

`transform-origin: calc(-38px) 16px`: sitúa el punto de giro 38 píxeles a la izquierda de la tapa y 16 píxeles desde su borde superior.

`transform`: centra horizontalmente la tapa, la eleva 26 píxeles y la deja inicialmente sin rotación.

`border-radius: 4px`: redondea ligeramente las esquinas.

`background`: crea franjas diagonales repetidas de 8 píxeles en blanco y morado oscuro `#6b21a8`.

`box-shadow`: dibuja una línea interior negra con 28 % de opacidad y una sombra exterior negra con 35 % de opacidad.

`animation`: ejecuta continuamente `clapOpenSep`, con una duración de 2.3 segundos y aceleración suave al inicio y al final.

---

```css
.tile-header-centered {
  justify-content: center;
}
```

`justify-content: center`: centra horizontalmente el contenido de un encabezado de tarjeta cuando este utiliza un contenedor Flexbox o Grid compatible.

## css/layout/film-rails.css

```css
.film-roll-vertical {
  position: fixed;
  top: 0;
  bottom: 0;
  width: var(--film-rail-width);
  background: linear-gradient(#0b0b0f, #151021);
  border-left: 2px solid var(--color-border-subtle);
  border-right: 2px solid var(--color-border-subtle);
  overflow: hidden;
  z-index: 2;
}
```

`position: fixed`: mantiene el riel sujeto a la ventana aunque la página se desplace.

`top: 0`: alinea el borde superior del riel con la parte superior de la ventana.

`bottom: 0`: extiende el riel hasta la parte inferior de la ventana.

`width: var(--film-rail-width)`: establece el ancho mediante `--film-rail-width`, cuyo valor actual es `140px`.

`background`: aplica un degradado vertical desde el negro azulado `#0b0b0f` hasta el morado oscuro `#151021`.

`border-left`: dibuja un borde izquierdo de 2 píxeles con `--color-border-subtle`, cuyo valor actual es `rgba(255,255,255,.12)`.

`border-right`: dibuja el mismo borde tenue en el lado derecho.

`overflow: hidden`: oculta las partes de perforaciones y pósteres que salen del riel.

`z-index: 2`: coloca los rieles por encima de elementos con un nivel de apilamiento menor.

---

```css
.film-roll-vertical.left {
  left: 0;
}
```

`left: 0`: fija la variante izquierda al borde izquierdo de la ventana.

---

```css
.film-roll-vertical.right {
  right: 0;
}
```

`right: 0`: fija la variante derecha al borde derecho de la ventana.

---

```css
.film-roll-vertical::before,
.film-roll-vertical::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  width: 14px;
  z-index: 3;
  pointer-events: none;
  background-image: linear-gradient(
    to bottom,
    #e7e7ea 0 var(--film-sprocket-hole-height),
    rgba(231,231,234,0) var(--film-sprocket-hole-height) var(--film-sprocket-pattern-step)
  );
  background-repeat: repeat-y;
  background-size: 100% var(--film-sprocket-pattern-step);
  background-position: 0 0;
  animation: sprocketMove var(--film-sprocket-cycle-duration) linear infinite;
}
```

`content: ""`: crea dos pseudoelementos vacíos para dibujar las filas de perforaciones.

`position: absolute`: permite colocar las perforaciones dentro del riel.

`top: 0`: inicia cada fila en la parte superior del riel.

`bottom: 0`: extiende cada fila hasta la parte inferior.

`width: 14px`: fija el ancho de cada fila de perforaciones.

`z-index: 3`: sitúa las perforaciones por encima del fondo y del carril de pósteres.

`pointer-events: none`: evita que los pseudoelementos intercepten clics o movimientos del puntero.

`background-image`: dibuja cada perforación con el gris claro `#e7e7ea` hasta la altura indicada por `--film-sprocket-hole-height`, actualmente `30px`, y deja transparente el resto hasta `--film-sprocket-pattern-step`, actualmente `66px`.

`background-repeat: repeat-y`: repite el patrón únicamente en dirección vertical.

`background-size: 100% var(--film-sprocket-pattern-step)`: hace que cada repetición ocupe todo el ancho y 66 píxeles de alto, según el valor actual de `--film-sprocket-pattern-step`.

`background-position: 0 0`: inicia el patrón en la esquina superior izquierda.

`animation`: desplaza continuamente las perforaciones mediante `sprocketMove`; `--film-sprocket-cycle-duration` contiene actualmente `1s`, por lo que cada ciclo dura un segundo y mantiene una velocidad constante.

---

```css
.film-roll-vertical::before {
  left: 6px;
}
```

`left: 6px`: coloca la primera fila de perforaciones a 6 píxeles del borde izquierdo del riel.

---

```css
.film-roll-vertical::after {
  right: 6px;
}
```

`right: 6px`: coloca la segunda fila de perforaciones a 6 píxeles del borde derecho del riel.

---

```css
.film-roll-vertical.left::before,
.film-roll-vertical.left::after {
  animation-direction: normal;
}
```

`animation-direction: normal`: ejecuta la animación de las perforaciones del riel izquierdo en el sentido definido originalmente.

---

```css
.film-roll-vertical.left .film-track-vertical {
  animation-direction: normal;
}
```

`animation-direction: normal`: desplaza el carril de pósteres izquierdo en el sentido original de `verticalScroll`.

---

```css
.film-roll-vertical.right::before,
.film-roll-vertical.right::after {
  animation-direction: reverse;
}
```

`animation-direction: reverse`: ejecuta hacia atrás la animación de las perforaciones del riel derecho.

---

```css
.film-roll-vertical.right .film-track-vertical {
  animation-direction: reverse;
}
```

`animation-direction: reverse`: desplaza el carril de pósteres derecho en sentido contrario al izquierdo.

---

```css
.film-track-vertical {
  position: absolute;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
  animation: verticalScroll 40s linear infinite;
}
```

`position: absolute`: permite mover el carril dentro del riel sin ocupar espacio en el flujo normal.

`left: 0`: alinea el carril con el borde izquierdo del riel.

`right: 0`: lo extiende hasta el borde derecho del riel.

`display: flex`: organiza los fotogramas mediante Flexbox.

`flex-direction: column`: coloca los fotogramas uno debajo de otro.

`gap: 20px`: deja 20 píxeles entre cada fotograma.

`animation`: ejecuta continuamente `verticalScroll` durante 40 segundos con velocidad constante.

---

```css
.frame-vertical {
  flex: 0 0 auto;
  margin: 0 auto;
  width: 100px;
  height: 150px;
  background: #0b0b0f;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.08), 0 6px 16px rgba(0,0,0,.45);
}
```

`flex: 0 0 auto`: impide que el fotograma crezca o se reduzca y conserva sus dimensiones declaradas.

`margin: 0 auto`: elimina el margen vertical y centra horizontalmente el fotograma.

`width: 100px`: fija el ancho del fotograma en 100 píxeles.

`height: 150px`: fija la altura del fotograma en 150 píxeles.

`background: #0b0b0f`: aplica un fondo negro azulado detrás de la imagen.

`border-radius: 8px`: redondea las esquinas del fotograma.

`overflow: hidden`: recorta la imagen y cualquier contenido que salga de las esquinas redondeadas.

`box-shadow`: añade una línea blanca interior con 8 % de opacidad y una sombra exterior negra con 45 % de opacidad.

---

```css
.frame-vertical img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```

`width: 100%`: hace que la imagen ocupe todo el ancho del fotograma.

`height: 100%`: hace que la imagen ocupe toda su altura.

`object-fit: cover`: llena el fotograma conservando la proporción de la imagen y recorta lo que sobresalga.

`display: block`: elimina el espacio inferior que pueden generar las imágenes en línea.

## css/layout/hero.css

```css
.hero {
  padding: 54px 0 24px;
}
```

`padding: 54px 0 24px`: añade 54 píxeles de espacio interno arriba, ninguno a los lados y 24 abajo.

---

```css
.hero-title {
  font-family: var(--brand-font);
  font-size: clamp(2.4rem, 6vw, 4.6rem);
  letter-spacing: 1px;
  line-height: 1;
  text-shadow: 0 12px 32px rgba(0,0,0,.6), 0 0 24px rgba(255,255,255,.16);
}
```

`font-family: var(--brand-font)`: aplica la tipografía de marca, cuyo valor actual es `'Bebas Neue', sans-serif`.

`font-size`: adapta el título entre `2.4rem` y `4.6rem`, usando `6vw` mientras se encuentre dentro de esos límites.

`letter-spacing: 1px`: separa las letras por un píxel.

`line-height: 1`: ajusta la altura de línea al mismo tamaño de la fuente.

`text-shadow`: añade una sombra negra amplia debajo del texto y un resplandor blanco tenue alrededor.

---

```css
.hero-sub {
  color: var(--color-text-secondary);
  font-family: var(--font-family-interface);
  font-size: clamp(1.05rem, 1.6vw, 1.25rem);
  letter-spacing: .4px;
  text-transform: uppercase;
}
```

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb` definido actualmente por `--color-text-secondary`.

`font-family: var(--font-family-interface)`: usa la tipografía de interfaz, cuyo valor actual es `'Teko', system-ui, sans-serif`.

`font-size`: adapta el subtítulo entre `1.05rem` y `1.25rem`, usando `1.6vw` dentro de esos límites.

`letter-spacing: .4px`: separa las letras por 0.4 píxeles.

`text-transform: uppercase`: muestra el subtítulo en mayúsculas.

## css/layout/page-shell.css

```css
.edit-page {
  position: relative;
  padding-top: 8px;
}
```

`position: relative`: mantiene la página en el flujo normal y permite posicionar elementos descendientes respecto a ella.

`padding-top: 8px`: añade 8 píxeles de espacio interno en la parte superior.

---

```css
.edit-bg {
  position: fixed;
  inset: 0;
  z-index: -2;
  --bg-img: var(--edit-bg, none);
  background-image:
    var(--bg-img),
    radial-gradient(1200px 600px at 20% 20%, rgba(155,92,251,.18), rgba(0,0,0,0)),
    radial-gradient(1000px 520px at 80% 80%, rgba(20,255,233,.12), rgba(0,0,0,0));
  background-size: cover, auto, auto;
  background-position: center;
  filter: blur(20px) saturate(120%);
  opacity: .35;
}
```

`position: fixed`: mantiene el fondo sujeto a la ventana durante el desplazamiento.

`inset: 0`: extiende el fondo hasta los cuatro bordes de la ventana.

`z-index: -2`: coloca el fondo dos niveles detrás de los elementos con nivel cero dentro del contexto de apilamiento correspondiente.

`--bg-img: var(--edit-bg, none)`: crea una variable local con la imagen proporcionada por `--edit-bg`; si no existe, usa `none` y no muestra imagen.

`background-image`: superpone la imagen de `--bg-img`, un resplandor morado con 18 % de opacidad en la zona superior izquierda y un resplandor cian con 12 % de opacidad en la zona inferior derecha.

`background-size: cover, auto, auto`: hace que la imagen cubra todo el fondo y conserva el tamaño calculado de los dos degradados.

`background-position: center`: centra las capas de fondo.

`filter`: desenfoca el fondo 20 píxeles y aumenta su saturación al 120 %.

`opacity: .35`: muestra toda la capa al 35 % de opacidad.

---

```css
.edit-glow {
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background:
    radial-gradient(900px 420px at 30% 30%, rgba(155,92,251,.16), transparent 70%),
    radial-gradient(700px 360px at 72% 70%, rgba(20,255,233,.12), transparent 70%);
  mix-blend-mode: screen;
  animation: glowDrift 8s ease-in-out infinite alternate;
}
```

`position: fixed`: mantiene el resplandor sujeto a la ventana.

`inset: 0`: extiende la capa hasta los cuatro bordes de la ventana.

`z-index: -1`: coloca el resplandor detrás del contenido y delante de `.edit-bg`, que usa `-2`.

`pointer-events: none`: evita que la capa intercepte interacciones del usuario.

`background`: superpone un resplandor morado con 16 % de opacidad y otro cian con 12 %, ambos desvanecidos hasta ser transparentes al 70 %.

`mix-blend-mode: screen`: aclara visualmente las capas que quedan detrás al mezclar los colores.

`animation`: ejecuta `glowDrift` durante ocho segundos, suaviza el inicio y el final, se repite indefinidamente y alterna el sentido en cada ciclo.

---

```css
.edit-page.is-vista .edit-glow {
  background:
    radial-gradient(900px 420px at 30% 30%, rgba(46,204,113,.20), transparent 70%),
    radial-gradient(700px 360px at 72% 70%, rgba(155,92,251,.12), transparent 70%);
}
```

`background`: cuando la página tiene el estado `is-vista`, reemplaza los resplandores generales por uno verde con 20 % de opacidad y otro morado con 12 %, ambos desvanecidos al 70 %.

---

```css
.edit-page.is-pendiente .edit-glow {
  background:
    radial-gradient(900px 420px at 30% 30%, rgba(231,76,60,.18), transparent 70%),
    radial-gradient(700px 360px at 72% 70%, rgba(155,92,251,.12), transparent 70%);
}
```

`background`: cuando la página tiene el estado `is-pendiente`, reemplaza los resplandores generales por uno rojo con 18 % de opacidad y otro morado con 12 %, ambos desvanecidos al 70 %.

---

```css
.edit-title {
  font-family: var(--brand-font);
  letter-spacing: .6px;
  text-shadow: 0 14px 28px rgba(0,0,0,.5);
  display: flex;
  align-items: center;
  gap: .6rem;
}
```

`font-family: var(--brand-font)`: aplica la tipografía de marca, cuyo valor actual es `'Bebas Neue', sans-serif`.

`letter-spacing: .6px`: separa las letras por 0.6 píxeles.

`text-shadow`: proyecta una sombra negra con 50 % de opacidad, desplazada 14 píxeles hacia abajo y difuminada 28 píxeles.

`display: flex`: coloca los elementos del título en una fila flexible.

`align-items: center`: centra verticalmente los elementos del título.

`gap: .6rem`: deja `0.6rem` de separación entre ellos.

---

```css
.edit-title small {
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .5px;
  color: var(--color-text-secondary);
}
```

`font-family: var(--font-family-interface)`: aplica la tipografía de interfaz, cuyo valor actual es `'Teko', system-ui, sans-serif`.

`text-transform: uppercase`: muestra en mayúsculas el texto secundario del título.

`letter-spacing: .5px`: separa sus letras por medio píxel.

`color: var(--color-text-secondary)`: aplica el lavanda claro `#dcd3fb` definido actualmente por `--color-text-secondary`.
## Variables de arquitectura del layout

`layout/film-rails.css` declara globalmente `--film-rail-width: 140px` y `--film-rail-content-offset: calc(var(--film-rail-width) + 18px)`. El alcance global permite que Film Rails, Cinedock y las reglas responsive compartan la misma geometría.

`.film-roll-vertical` declara localmente `--film-sprocket-cycle-duration: 1s`, `--film-sprocket-pattern-step: 66px` y `--film-sprocket-hole-height: 30px`; sus pseudoelementos las reciben por herencia.

`layout/clapboard.css` declara las cuatro variables `--clapboard-*` sobre el alcance compartido `.clap-sep, .logo-claqueta-anim`. El separador y el logotipo comparten una sola definición sin exponer esos valores en `:root`.
