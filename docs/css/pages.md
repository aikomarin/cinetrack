## css/pages/home.css

La variante local `.tile-header-centered` fue sustituida en los estados vacíos por la utilidad de Bootstrap `.justify-content-center`. La clase base `.tile-header` continúa aportando el contenedor flex, la alineación vertical y el gap; la utilidad conserva el mismo `justify-content: center`.


.dash-grid {
  display: grid;
  grid-template-areas:
    "ring  bars  movies  series"
    "ring  prog  favs   total";
  grid-template-columns: 1.3fr 1.7fr 1fr 1fr;
  gap: 16px;
  margin-bottom: 28px;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-areas: "ring bars movies series" "ring prog favs total"`: define la distribución nominal de las áreas de la cuadrícula.

`grid-template-columns: 1.3fr 1.7fr 1fr 1fr`: define las columnas de la cuadrícula con `1.3fr 1.7fr 1fr 1fr`.

`gap: 16px`: deja una separación de `16px` entre elementos.

`margin-bottom: 28px`: deja un margen inferior de `28px`.

---

```css
.dash-grid > .tile:nth-child(1) {
  grid-area: ring;
}
```

`grid-area: ring`: coloca el elemento en el área `ring` de la cuadrícula.

---

```css
.dash-grid > .tile:nth-child(2) {
  grid-area: bars;
}
```

`grid-area: bars`: coloca el elemento en el área `bars` de la cuadrícula.

---

```css
.dash-grid > .tile:nth-child(3) {
  grid-area: prog;
}
```

`grid-area: prog`: coloca el elemento en el área `prog` de la cuadrícula.

---

```css
.dash-grid > .tile:nth-child(4) {
  grid-area: movies;
}
```

`grid-area: movies`: coloca el elemento en el área `movies` de la cuadrícula.

---

```css
.dash-grid > .tile:nth-child(5) {
  grid-area: series;
}
```

`grid-area: series`: coloca el elemento en el área `series` de la cuadrícula.

---

```css
.dash-grid > .tile:nth-child(6) {
  grid-area: favs;
}
```

`grid-area: favs`: coloca el elemento en el área `favs` de la cuadrícula.

---

```css
.dash-grid > .tile:nth-child(7) {
  grid-area: total;
}
```

`grid-area: total`: coloca el elemento en el área `total` de la cuadrícula.

---

```css
.tile-ring {
  grid-area: ring;
}
```

`grid-area: ring`: coloca el elemento en el área `ring` de la cuadrícula.

---

```css
.tile.tile-ring {
  display: grid;
  grid-template-areas:
    "head"
    "donut"
    "sub";
  justify-items: center;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-areas: "head" "donut" "sub"`: define la distribución nominal de las áreas de la cuadrícula.

`justify-items: center`: alinea los elementos de la cuadrícula mediante `center`.

---

```css
.tile-ring .tile-header {
  grid-area: head;
  width: 100%;
}
```

`grid-area: head`: coloca el elemento en el área `head` de la cuadrícula.

`width: 100%`: establece el ancho en `100%`.

---

```css
.tile-ring .ring {
  grid-area: donut;
}
```

`grid-area: donut`: coloca el elemento en el área `donut` de la cuadrícula.

---

```css
.tile-ring .ring-center {
  grid-area: donut;
  position: static;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0;
}
```

`grid-area: donut`: coloca el elemento en el área `donut` de la cuadrícula.

`position: static`: utiliza posicionamiento `static`.

`display: flex`: establece el modelo de presentación como `flex`.

`flex-direction: column`: organiza los elementos flexibles en dirección `column`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: center`: distribuye los elementos mediante `center`.

`margin: 0`: aplica el margen exterior `0`.

---

```css
.tile-ring .ring-sub {
  grid-area: sub;
}
```

`grid-area: sub`: coloca el elemento en el área `sub` de la cuadrícula.

---

```css
.tile-bars {
  grid-area: bars;
}
```

`grid-area: bars`: coloca el elemento en el área `bars` de la cuadrícula.

---

```css
.tile-progress {
  grid-area: prog;
}
```

`grid-area: prog`: coloca el elemento en el área `prog` de la cuadrícula.

---

```css
.metric-total {
  grid-area: total;
}
```

`grid-area: total`: coloca el elemento en el área `total` de la cuadrícula.

---

```css
.metric-movies {
  grid-area: movies;
}
```

`grid-area: movies`: coloca el elemento en el área `movies` de la cuadrícula.

---

```css
.metric-series {
  grid-area: series;
}
```

`grid-area: series`: coloca el elemento en el área `series` de la cuadrícula.

---

```css
.metric-favs {
  grid-area: favs;
}
```

`grid-area: favs`: coloca el elemento en el área `favs` de la cuadrícula.

---

```css
.ring {
  grid-area: donut;
  width: 220px;
  height: 220px;
  margin: 0;
  background: transparent !important;
}
```

`grid-area: donut`: coloca el elemento en el área `donut` de la cuadrícula.

`width: 220px`: establece el ancho en `220px`.

`height: 220px`: establece la altura en `220px`.

`margin: 0`: aplica el margen exterior `0`.

`background: transparent !important`: aplica el fondo `transparent !important`.

---

```css
.ring-bg {
  fill: none;
  stroke: rgba(255,255,255,.12);
  stroke-width: 12;
}
```

`fill: none`: aplica el relleno SVG `none`.

`stroke: rgba(255,255,255,.12)`: aplica el trazo SVG `rgba(255,255,255,.12)`.

`stroke-width: 12`: fija el ancho del trazo SVG en `12`.

---

```css
.ring-val {
  fill: none;
  stroke: var(--accent);
  stroke-width: 12;
  stroke-linecap: round;
  stroke-dasharray: 326;
  transition: stroke-dashoffset .8s ease;
  filter: none !important;    
}
```

`fill: none`: aplica el relleno SVG `none`.

`stroke: var(--accent)`: aplica el trazo SVG `var(--accent)`.

`stroke-width: 12`: fija el ancho del trazo SVG en `12`.

`stroke-linecap: round`: define los extremos del trazo como `round`.

`stroke-dasharray: 326`: define el patrón discontinuo del trazo como `326`.

`transition: stroke-dashoffset .8s ease`: suaviza los cambios indicados mediante `stroke-dashoffset .8s ease`.

`filter: none !important`: aplica el filtro visual `none !important`.

---

```css
.ring-center {
  grid-area: donut;
  position: static;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  pointer-events: none;
  background: transparent !important;
}
```

`grid-area: donut`: coloca el elemento en el área `donut` de la cuadrícula.

`position: static`: utiliza posicionamiento `static`.

`display: flex`: establece el modelo de presentación como `flex`.

`flex-direction: column`: organiza los elementos flexibles en dirección `column`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: center`: distribuye los elementos mediante `center`.

`pointer-events: none`: configura la interacción del puntero como `none`.

`background: transparent !important`: aplica el fondo `transparent !important`.

---

```css
.ring-number {
  font-size: 3rem;
  font-weight: 900;
  line-height: 1;
}
```

`font-size: 3rem`: establece el tamaño de fuente en `3rem`.

`font-weight: 900`: aplica el grosor tipográfico `900`.

`line-height: 1`: establece la altura de línea en `1`.

---

```css
.ring-caption {
  font-family: var(--font-family-interface);
  opacity: .8;
  margin-top: -2px;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica `var(--font-family-interface)`.

`opacity: .8`: muestra el elemento con una opacidad de `.8`.

`margin-top: -2px`: deja un margen superior de `-2px`.

---

```css
.ring-sub {
  grid-area: sub;
  margin-top: 8px;
}
```

`grid-area: sub`: coloca el elemento en el área `sub` de la cuadrícula.

`margin-top: 8px`: deja un margen superior de `8px`.

---

```css
.bars {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 6px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`flex-direction: column`: organiza los elementos flexibles en dirección `column`.

`gap: 10px`: deja una separación de `10px` entre elementos.

`margin-top: 6px`: deja un margen superior de `6px`.

---

```css
.bar {
  display: grid;
  grid-template-columns: 1fr auto 42px;
  gap: 10px;
  align-items: center;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-columns: 1fr auto 42px`: define las columnas de la cuadrícula con `1fr auto 42px`.

`gap: 10px`: deja una separación de `10px` entre elementos.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

---

```css
.bar .label {
  font-weight: 700;
}
```

`font-weight: 700`: aplica el grosor tipográfico `700`.

---

```css
.bar .track {
  position: relative;
  height: 12px;
  border-radius: 999px;
  background: rgba(255,255,255,.08);
  border: 1px solid var(--color-border-subtle);
  overflow: hidden;
  --delay: 0s;
}
```

`position: relative`: utiliza posicionamiento `relative`.

`height: 12px`: establece la altura en `12px`.

`border-radius: 999px`: redondea las esquinas con `999px`.

`background: rgba(255,255,255,.08)`: aplica el fondo `rgba(255,255,255,.08)`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

`overflow: hidden`: controla el contenido desbordado mediante `hidden`.

`--delay: 0s`: define la variable local `--delay` con el valor `0s`.

---

```css
.bar:nth-child(2) .track {
  --delay: .08s;
}
```

`--delay: .08s`: define la variable local `--delay` con el valor `.08s`.

---

```css
.bar:nth-child(3) .track {
  --delay: .16s;
}
```

`--delay: .16s`: define la variable local `--delay` con el valor `.16s`.

---

```css
.bar:nth-child(4) .track {
  --delay: .24s;
}
```

`--delay: .24s`: define la variable local `--delay` con el valor `.24s`.

---

```css
.bar:nth-child(5) .track {
  --delay: .32s;
}
```

`--delay: .32s`: define la variable local `--delay` con el valor `.32s`.

---

```css
.bar .fill {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 0;
  background: linear-gradient(90deg, var(--accent), var(--color-accent-dark));
  animation: growBar 1.1s ease forwards;
  animation-delay: var(--delay);
}
```

`position: absolute`: utiliza posicionamiento `absolute`.

`left: 0`: sitúa el borde izquierdo en `0`.

`top: 0`: sitúa el borde superior en `0`.

`bottom: 0`: sitúa el borde inferior en `0`.

`width: 0`: establece el ancho en `0`.

`background: linear-gradient(90deg, var(--accent), var(--color-accent-dark))`: aplica el fondo `linear-gradient(90deg, var(--accent), var(--color-accent-dark))`.

`animation: growBar 1.1s ease forwards`: ejecuta la animación `growBar 1.1s ease forwards`.

`animation-delay: var(--delay)`: retrasa la animación `var(--delay)`.

---

```css
.bar .value {
  font-weight: 800;
  text-align: right;
}
```

`font-weight: 800`: aplica el grosor tipográfico `800`.

`text-align: right`: alinea el texto hacia `right`.

---

```css
.progress-meta {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-family: var(--font-family-interface);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: .4px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`justify-content: space-between`: distribuye los elementos mediante `space-between`.

`gap: 12px`: deja una separación de `12px` entre elementos.

`font-family: var(--font-family-interface)`: aplica la familia tipográfica `var(--font-family-interface)`.

`color: var(--color-text-secondary)`: aplica el color `var(--color-text-secondary)` al contenido.

`text-transform: uppercase`: transforma visualmente el texto mediante `uppercase`.

`font-weight: 700`: aplica el grosor tipográfico `700`.

`letter-spacing: .4px`: separa las letras `.4px`.

---

```css
.progress-rail {
  margin-top: 10px;
  height: 16px;
  border-radius: 999px;
  background: rgba(255,255,255,.08);
  border: 1px solid var(--color-border-subtle);
  overflow: hidden;
  position: relative;
}
```

`margin-top: 10px`: deja un margen superior de `10px`.

`height: 16px`: establece la altura en `16px`.

`border-radius: 999px`: redondea las esquinas con `999px`.

`background: rgba(255,255,255,.08)`: aplica el fondo `rgba(255,255,255,.08)`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

`overflow: hidden`: controla el contenido desbordado mediante `hidden`.

`position: relative`: utiliza posicionamiento `relative`.

---

```css
.progress-fill {
  position: absolute;
  inset: 0;
  width: 0;
  background: linear-gradient(90deg, var(--accent), var(--color-accent-dark));
  animation: fillProg 1.2s ease forwards;
}
```

`position: absolute`: utiliza posicionamiento `absolute`.

`inset: 0`: sitúa los cuatro bordes con el valor `0`.

`width: 0`: establece el ancho en `0`.

`background: linear-gradient(90deg, var(--accent), var(--color-accent-dark))`: aplica el fondo `linear-gradient(90deg, var(--accent), var(--color-accent-dark))`.

`animation: fillProg 1.2s ease forwards`: ejecuta la animación `fillProg 1.2s ease forwards`.

---

```css
.progress-caption {
  margin-top: 6px;
  color: var(--color-text-secondary);
}
```

`margin-top: 6px`: deja un margen superior de `6px`.

`color: var(--color-text-secondary)`: aplica el color `var(--color-text-secondary)` al contenido.

---

```css
.metric {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 6px;
  min-height: 120px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`flex-direction: column`: organiza los elementos flexibles en dirección `column`.

`justify-content: center`: distribuye los elementos mediante `center`.

`align-items: flex-start`: alinea los elementos en el eje transversal mediante `flex-start`.

`gap: 6px`: deja una separación de `6px` entre elementos.

`min-height: 120px`: impide que la altura sea menor que `120px`.

---

```css
.metric-icon {
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  margin-bottom: 2px;
  background: rgba(255,255,255,.08);
  border: 1px solid var(--color-border-subtle);
}
```

`width: 36px`: establece el ancho en `36px`.

`height: 36px`: establece la altura en `36px`.

`display: grid`: establece el modelo de presentación como `grid`.

`place-items: center`: alinea el contenido de Grid mediante `center`.

`border-radius: 10px`: redondea las esquinas con `10px`.

`margin-bottom: 2px`: deja un margen inferior de `2px`.

`background: rgba(255,255,255,.08)`: aplica el fondo `rgba(255,255,255,.08)`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

---

```css
.metric-label {
  font-family: var(--font-family-interface);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: .5px;
  font-weight: 700;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica `var(--font-family-interface)`.

`color: var(--color-text-secondary)`: aplica el color `var(--color-text-secondary)` al contenido.

`text-transform: uppercase`: transforma visualmente el texto mediante `uppercase`.

`letter-spacing: .5px`: separa las letras `.5px`.

`font-weight: 700`: aplica el grosor tipográfico `700`.

---

```css
.metric-value {
  font-size: 1.8rem;
  font-weight: 900;
}
```

`font-size: 1.8rem`: establece el tamaño de fuente en `1.8rem`.

`font-weight: 900`: aplica el grosor tipográfico `900`.

---

```css
.toprated-section {
  margin-top: 20px;
  margin-bottom: 56px;
  position: relative;
}
```

`margin-top: 20px`: deja un margen superior de `20px`.

`margin-bottom: 56px`: deja un margen inferior de `56px`.

`position: relative`: utiliza posicionamiento `relative`.

---

```css
.toprated-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 8px 0 12px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: space-between`: distribuye los elementos mediante `space-between`.

`margin: 8px 0 12px`: aplica el margen exterior `8px 0 12px`.

---

```css
.toprated-rail {
  --gap: 14px;
  display: flex;
  gap: var(--gap);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding-bottom: 6px;
  scrollbar-width: thin;
}
```

`--gap: 14px`: define la variable local `--gap` con el valor `14px`.

`display: flex`: establece el modelo de presentación como `flex`.

`gap: var(--gap)`: deja una separación de `var(--gap)` entre elementos.

`overflow-x: auto`: controla horizontalmente el desbordamiento mediante `auto`.

`scroll-snap-type: x mandatory`: configura el ajuste del desplazamiento como `x mandatory`.

`padding-bottom: 6px`: establece `padding-bottom` en `6px`.

`scrollbar-width: thin`: establece el grosor de la barra como `thin`.

---

```css
.toprated-rail::-webkit-scrollbar {
  height: 8px;
}
```

`height: 8px`: establece la altura en `8px`.

---

```css
.toprated-rail::-webkit-scrollbar-thumb {
  background: rgba(255,255,255,.18);
  border-radius: 10px;
}
```

`background: rgba(255,255,255,.18)`: aplica el fondo `rgba(255,255,255,.18)`.

`border-radius: 10px`: redondea las esquinas con `10px`.

---

```css
.recent-section {
  margin-top: 10px;
}
```

`margin-top: 10px`: deja un margen superior de `10px`.

---

```css
.recent-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 6px 0 10px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: space-between`: distribuye los elementos mediante `space-between`.

`margin: 6px 0 10px`: aplica el margen exterior `6px 0 10px`.

---

```css
.recent-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 14px;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-columns: repeat(12, 1fr)`: define las columnas de la cuadrícula con `repeat(12, 1fr)`.

`gap: 14px`: deja una separación de `14px` entre elementos.

---

```css
.recent-card {
  display: grid;
  grid-template-rows: auto 1fr;
  background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04));
  border: 1px solid var(--color-border-subtle);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 12px 24px rgba(0,0,0,.35);
  transition: transform .15s ease, box-shadow .2s ease;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-rows: auto 1fr`: define las filas de la cuadrícula con `auto 1fr`.

`background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04))`: aplica el fondo `linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04))`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

`border-radius: 16px`: redondea las esquinas con `16px`.

`overflow: hidden`: controla el contenido desbordado mediante `hidden`.

`box-shadow: 0 12px 24px rgba(0,0,0,.35)`: aplica la sombra `0 12px 24px rgba(0,0,0,.35)`.

`transition: transform .15s ease, box-shadow .2s ease`: suaviza los cambios indicados mediante `transform .15s ease, box-shadow .2s ease`.

---

```css
.recent-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 28px rgba(0,0,0,.45);
}
```

`transform: translateY(-2px)`: aplica la transformación `translateY(-2px)`.

`box-shadow: 0 16px 28px rgba(0,0,0,.45)`: aplica la sombra `0 16px 28px rgba(0,0,0,.45)`.

---

```css
.recent-thumb {
  position: relative;
  aspect-ratio: 2/3;
  background: #0b0b0f;
}
```

`position: relative`: utiliza posicionamiento `relative`.

`aspect-ratio: 2/3`: mantiene la proporción `2/3`.

`background: #0b0b0f`: aplica el fondo `#0b0b0f`.

---

```css
.recent-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```

`width: 100%`: establece el ancho en `100%`.

`height: 100%`: establece la altura en `100%`.

`object-fit: cover`: ajusta el contenido reemplazado mediante `cover`.

`display: block`: establece el modelo de presentación como `block`.

---

```css
.recent-thumb-ph {
  width: 100%;
  height: 100%;
  display: grid;
  place-items: center;
  color: #9aa;
  font-size: 1.6rem;
}
```

`width: 100%`: establece el ancho en `100%`.

`height: 100%`: establece la altura en `100%`.

`display: grid`: establece el modelo de presentación como `grid`.

`place-items: center`: alinea el contenido de Grid mediante `center`.

`color: #9aa`: aplica el color `#9aa` al contenido.

`font-size: 1.6rem`: establece el tamaño de fuente en `1.6rem`.

---

```css
.recent-meta {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 10px 12px 12px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`flex-direction: column`: organiza los elementos flexibles en dirección `column`.

`gap: 6px`: deja una separación de `6px` entre elementos.

`padding: 10px 12px 12px`: aplica el espacio interior `10px 12px 12px`.

---

```css
.recent-name {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 800;
  line-height: 1.1;
  max-height: 2.2em;
  overflow: hidden;
}
```

`margin: 0`: aplica el margen exterior `0`.

`font-size: 1.05rem`: establece el tamaño de fuente en `1.05rem`.

`font-weight: 800`: aplica el grosor tipográfico `800`.

`line-height: 1.1`: establece la altura de línea en `1.1`.

`max-height: 2.2em`: limita la altura a `2.2em`.

`overflow: hidden`: controla el contenido desbordado mediante `hidden`.

---

```css
.recent-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`flex-wrap: wrap`: controla el salto de los elementos flexibles mediante `wrap`.

`gap: 6px`: deja una separación de `6px` entre elementos.

---

```css
.recent-tags .tag {
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing:.5px;
  font-weight:700;
  font-size:.8rem;
  padding:.12rem .5rem;
  border-radius:999px;
  border:1px solid var(--color-border-subtle);
  background: rgba(255,255,255,.04);
  color: var(--color-text-secondary);
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica `var(--font-family-interface)`.

`text-transform: uppercase`: transforma visualmente el texto mediante `uppercase`.

`letter-spacing: .5px`: separa las letras `.5px`.

`font-weight: 700`: aplica el grosor tipográfico `700`.

`font-size: .8rem`: establece el tamaño de fuente en `.8rem`.

`padding: .12rem .5rem`: aplica el espacio interior `.12rem .5rem`.

`border-radius: 999px`: redondea las esquinas con `999px`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

`background: rgba(255,255,255,.04)`: aplica el fondo `rgba(255,255,255,.04)`.

`color: var(--color-text-secondary)`: aplica el color `var(--color-text-secondary)` al contenido.

---

```css
.recent-foot {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
```

`margin-top: auto`: deja un margen superior de `auto`.

`display: flex`: establece el modelo de presentación como `flex`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: space-between`: distribuye los elementos mediante `space-between`.

`gap: 10px`: deja una separación de `10px` entre elementos.

---

```css
.recent-date {
  color: var(--color-text-secondary);
  font-size:.9rem;
}
```

`color: var(--color-text-secondary)`: aplica el color `var(--color-text-secondary)` al contenido.

`font-size: .9rem`: establece el tamaño de fuente en `.9rem`.

---

```css
.plat-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px 26px;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-columns: repeat(2, 1fr)`: define las columnas de la cuadrícula con `repeat(2, 1fr)`.

`gap: 20px 26px`: deja una separación de `20px 26px` entre elementos.

---

```css
.plat-tile {
  background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04));
  border: 1px solid var(--color-border-subtle);
  border-radius: 16px;
  padding: 14px 10px;
  box-shadow: 0 12px 24px rgba(0,0,0,.35);
  overflow: hidden;
}
```

`background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04))`: aplica el fondo `linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.04))`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

`border-radius: 16px`: redondea las esquinas con `16px`.

`padding: 14px 10px`: aplica el espacio interior `14px 10px`.

`box-shadow: 0 12px 24px rgba(0,0,0,.35)`: aplica la sombra `0 12px 24px rgba(0,0,0,.35)`.

`overflow: hidden`: controla el contenido desbordado mediante `hidden`.

---

```css
.plat-tile-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0 4px 10px;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: space-between`: distribuye los elementos mediante `space-between`.

`margin: 0 4px 10px`: aplica el margen exterior `0 4px 10px`.

---

```css
.plat-name {
  font-weight: 900;
  letter-spacing: .4px;
}
```

`font-weight: 900`: aplica el grosor tipográfico `900`.

`letter-spacing: .4px`: separa las letras `.4px`.

---

```css
.plat-count {
  display: none !important;
}
```

`display: none !important`: establece el modelo de presentación como `none !important`.

---

```css
.plat-mini-rail {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 12px;
  align-items: start;
  justify-items: center;
  margin: 0;
  padding: 0;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`grid-template-columns: repeat(5, minmax(0, 1fr))`: define las columnas de la cuadrícula con `repeat(5, minmax(0, 1fr))`.

`gap: 12px`: deja una separación de `12px` entre elementos.

`align-items: start`: alinea los elementos en el eje transversal mediante `start`.

`justify-items: center`: alinea los elementos de la cuadrícula mediante `center`.

`margin: 0`: aplica el margen exterior `0`.

`padding: 0`: aplica el espacio interior `0`.

---

```css
.plat-mini-rail > .plat-mini-item:nth-child(n+6) {
  display: none;
}
```

`display: none`: establece el modelo de presentación como `none`.

---

```css
.plat-mini-item {
  display: flex;
  flex-direction: column;
  width: 100%;
}
```

`display: flex`: establece el modelo de presentación como `flex`.

`flex-direction: column`: organiza los elementos flexibles en dirección `column`.

`width: 100%`: establece el ancho en `100%`.

---

```css
.plat-mini-card {
  width: 100%;
  aspect-ratio: 2 / 3;
  border-radius: 10px;
  overflow: hidden;
  background: #0b0b0f;
  border: 1px solid var(--color-border-subtle);
  box-shadow: 0 8px 16px rgba(0,0,0,.35);
  color: inherit;
  text-decoration: none;
}
```

`width: 100%`: establece el ancho en `100%`.

`aspect-ratio: 2 / 3`: mantiene la proporción `2 / 3`.

`border-radius: 10px`: redondea las esquinas con `10px`.

`overflow: hidden`: controla el contenido desbordado mediante `hidden`.

`background: #0b0b0f`: aplica el fondo `#0b0b0f`.

`border: 1px solid var(--color-border-subtle)`: dibuja el borde `1px solid var(--color-border-subtle)`.

`box-shadow: 0 8px 16px rgba(0,0,0,.35)`: aplica la sombra `0 8px 16px rgba(0,0,0,.35)`.

`color: inherit`: aplica el color `inherit` al contenido.

`text-decoration: none`: aplica la decoración de texto `none`.

---

```css
.plat-mini-card:hover {
  color: #fff;
  transform: translateY(-2px);
  box-shadow: 0 12px 20px rgba(0,0,0,.45);
}
```

`color: #fff`: aplica el color `#fff` al contenido.

`transform: translateY(-2px)`: aplica la transformación `translateY(-2px)`.

`box-shadow: 0 12px 20px rgba(0,0,0,.45)`: aplica la sombra `0 12px 20px rgba(0,0,0,.45)`.

---

```css
.plat-mini-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```

`width: 100%`: establece el ancho en `100%`.

`height: 100%`: establece la altura en `100%`.

`object-fit: cover`: ajusta el contenido reemplazado mediante `cover`.

`display: block`: establece el modelo de presentación como `block`.

---

```css
.plat-mini-title {
  display: none !important;
}
```

`display: none !important`: establece el modelo de presentación como `none !important`.

---

```css
.plat-rank {
  display: none !important;
}
```

`display: none !important`: establece el modelo de presentación como `none !important`.

## css/pages/catalog.css

```css
.filter-chips {
  padding-top: 14px;
}
```

`padding-top: 14px`: deja `14px` de espacio interior superior.

---

```css
.filter-chips .badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1.2;
  padding: .4rem .9rem;
  font-weight: 600;
}
```

`display: inline-flex`: establece el modelo de presentación como `inline-flex`.

`align-items: center`: alinea los elementos en el eje transversal mediante `center`.

`justify-content: center`: distribuye los elementos mediante `center`.

`line-height: 1.2`: establece la altura de línea en `1.2`.

`padding: .4rem .9rem`: aplica el espacio interior `.4rem .9rem`.

`font-weight: 600`: aplica el grosor tipográfico `600`.

---

```css
.group-count {
  background: var(--brand-purple, #7c3aed);
  color: #fff;
  font-weight: 600;
  font-size: 0.75rem;
  padding: 0.35rem 0.6rem;
}
```

`background: var(--brand-purple, #7c3aed)`: aplica el fondo `var(--brand-purple, #7c3aed)`.

`color: #fff`: aplica el color `#fff` al contenido.

`font-weight: 600`: aplica el grosor tipográfico `600`.

`font-size: 0.75rem`: establece el tamaño de fuente en `0.75rem`.

`padding: 0.35rem 0.6rem`: aplica el espacio interior `0.35rem 0.6rem`.

## css/pages/search.css

```css
.tile form .form-label {
  font-size: .9rem;
  margin-bottom: .45rem;
  letter-spacing: .2px;
}
```

`font-size: .9rem`: establece el tamaño de fuente en `.9rem`.

`margin-bottom: .45rem`: deja un margen inferior de `.45rem`.

`letter-spacing: .2px`: separa las letras `.2px`.

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

`background-color: rgba(255,255,255,.03)`: aplica el color de fondo `rgba(255,255,255,.03)`.

`border: 1px solid rgba(255,255,255,.14)`: dibuja el borde `1px solid rgba(255,255,255,.14)`.

`border-radius: 12px`: redondea las esquinas con `12px`.

`color: #fff`: aplica el color `#fff` al contenido.

`padding: .6rem .8rem`: aplica el espacio interior `.6rem .8rem`.

`font-size: 1rem`: establece el tamaño de fuente en `1rem`.

`-webkit-text-fill-color: #fff`: fuerza en Safari el color interno del texto a `#fff`.

---

```css
.tile form .form-control:focus {
  border-color: rgba(168,85,247,.6);
  box-shadow: 0 0 0 .2rem rgba(168,85,247,.15);
  outline: 0;
}
```

`border-color: rgba(168,85,247,.6)`: establece el color del borde en `rgba(168,85,247,.6)`.

`box-shadow: 0 0 0 .2rem rgba(168,85,247,.15)`: aplica la sombra `0 0 0 .2rem rgba(168,85,247,.15)`.

`outline: 0`: aplica el contorno `0`.

---

```css
.tile form .form-control::placeholder {
  color: rgba(255,255,255,.62);
  opacity: 1;
}
```

`color: rgba(255,255,255,.62)`: aplica el color `rgba(255,255,255,.62)` al contenido.

`opacity: 1`: muestra el elemento con una opacidad de `1`.

---

```css
.tile form .form-control::-webkit-input-placeholder {
  color: rgba(255,255,255,.62);
}
```

`color: rgba(255,255,255,.62)`: aplica el color `rgba(255,255,255,.62)` al contenido.

---

```css
.tile form .col-12.col-md-9:has(input[name="query"]) > .form-label {
  font-size: 1.3rem;
  line-height: 1.15;
  margin-bottom: .55rem;
  letter-spacing: .4px;
  font-weight: 700;
}
```

`font-size: 1.3rem`: establece el tamaño de fuente en `1.3rem`.

`line-height: 1.15`: establece la altura de línea en `1.15`.

`margin-bottom: .55rem`: deja un margen inferior de `.55rem`.

`letter-spacing: .4px`: separa las letras `.4px`.

`font-weight: 700`: aplica el grosor tipográfico `700`.

---

```css
.form-check.form-switch {
  min-width: 150px;
}
```

`min-width: 150px`: establece `min-width` en `150px`.

---

```css
.form-check.form-switch .form-check-input {
  cursor: pointer;
}
```

`cursor: pointer`: establece `cursor` en `pointer`.

---

```css
.form-check.form-switch .form-check-label {
  cursor: pointer;
  user-select: none;
}
```

`cursor: pointer`: establece `cursor` en `pointer`.

`user-select: none`: configura la selección de texto como `none`.

---

`.detail-poster`, su imagen y su estado hover utilizan ahora la base compartida documentada en `css/components/posters.css`. Search conserva aquí únicamente la variante contextual `.detail-poster.detail-poster-ph`.

---

```css
.detail-poster.detail-poster-ph {
  display: grid;
  place-items: center;
  color: rgba(255,255,255,.45);
  font-size: 2rem;
}
```

`display: grid`: establece el modelo de presentación como `grid`.

`place-items: center`: alinea el contenido de Grid mediante `center`.

`color: rgba(255,255,255,.45)`: aplica el color `rgba(255,255,255,.45)` al contenido.

`font-size: 2rem`: establece el tamaño de fuente en `2rem`.

---

```css
.detail-text {
  font-size: .975rem;
  line-height: 1.55;
  color: var(--color-text-primary, #e9e9e9);
  opacity: .92;
}
```

`font-size: .975rem`: establece el tamaño de fuente en `.975rem`.

`line-height: 1.55`: establece la altura de línea en `1.55`.

`color: var(--color-text-primary, #e9e9e9)`: aplica el color `var(--color-text-primary, #e9e9e9)` al contenido.

`opacity: .92`: muestra el elemento con una opacidad de `.92`.

---

```css
.tile p.success, .tile p.info, .tile p.warning, .tile p.error {
  margin: 0 0 .25rem 0;
}
```

`margin: 0 0 .25rem 0`: aplica el margen exterior `0 0 .25rem 0`.

---

```css
.tile p.success {
  color: #79ffa8;
}
```

`color: #79ffa8`: aplica el color `#79ffa8` al contenido.

---

```css
.tile p.info {
  color: #9ad1ff;
}
```

`color: #9ad1ff`: aplica el color `#9ad1ff` al contenido.

---

```css
.tile p.warning {
  color: #ffd27a;
}
```

`color: #ffd27a`: aplica el color `#ffd27a` al contenido.

---

```css
.tile p.error {
  color: #ff9a9a;
}
```

`color: #ff9a9a`: aplica el color `#ff9a9a` al contenido.

---

```css
.edit-card input[name="favorita"].form-check-input:checked {
  background-color: #ffd700;
  border-color: rgba(0,0,0,.15);
}
```

`background-color: #ffd700`: aplica el color de fondo `#ffd700`.

`border-color: rgba(0,0,0,.15)`: establece el color del borde en `rgba(0,0,0,.15)`.

## css/pages/detail.css

```css
.detail-page {
  position: relative;
  padding-top: 12px;
}
```

`position: relative`: establece el tipo de posicionamiento con el valor `relative`.

`padding-top: 12px`: aplica el espacio interior superior con el valor `12px`.

---

```css
.detail-bg {
  position: fixed;
  inset: 0;
  z-index: -2;
  --bg-img: var(--detail-bg, none);
  background-image:
    var(--bg-img),
    radial-gradient(1200px 600px at 20% 20%, rgba(155,92,251,.18), transparent),
    radial-gradient(1000px 520px at 80% 80%, rgba(20,255,233,.12), transparent);
  background-size: cover, auto, auto;
  background-position: center;
  filter: blur(22px) saturate(125%);
  opacity: .35;
}
```

`position: fixed`: establece el tipo de posicionamiento con el valor `fixed`.

`inset: 0`: sitúa los cuatro bordes con el valor `0`.

`z-index: -2`: establece el nivel de apilamiento con el valor `-2`.

`--bg-img: var(--detail-bg, none)`: establece `--bg-img` con el valor `var(--detail-bg, none)`.

`background-image: var(--bg-img), radial-gradient(1200px 600px at 20% 20%, rgba(155,92,251,.18), transparent), radial-gradient(1000px 520px at 80% 80%, rgba(20,255,233,.12), transparent)`: aplica las capas de imagen de fondo con el valor `var(--bg-img), radial-gradient(1200px 600px at 20% 20%, rgba(155,92,251,.18), transparent), radial-gradient(1000px 520px at 80% 80%, rgba(20,255,233,.12), transparent)`.

`background-size: cover, auto, auto`: define el tamaño de las capas de fondo con el valor `cover, auto, auto`.

`background-position: center`: define la posición del fondo con el valor `center`.

`filter: blur(22px) saturate(125%)`: aplica el filtro visual con el valor `blur(22px) saturate(125%)`.

`opacity: .35`: establece la opacidad con el valor `.35`.

---

```css
.detail-glow {
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

`position: fixed`: establece el tipo de posicionamiento con el valor `fixed`.

`inset: 0`: sitúa los cuatro bordes con el valor `0`.

`z-index: -1`: establece el nivel de apilamiento con el valor `-1`.

`pointer-events: none`: controla las interacciones del puntero con el valor `none`.

`background: radial-gradient(900px 420px at 30% 30%, rgba(155,92,251,.16), transparent 70%), radial-gradient(700px 360px at 72% 70%, rgba(20,255,233,.12), transparent 70%)`: aplica el fondo con el valor `radial-gradient(900px 420px at 30% 30%, rgba(155,92,251,.16), transparent 70%), radial-gradient(700px 360px at 72% 70%, rgba(20,255,233,.12), transparent 70%)`.

`mix-blend-mode: screen`: define el modo de mezcla visual con el valor `screen`.

`animation: glowDrift 8s ease-in-out infinite alternate`: ejecuta la animación con el valor `glowDrift 8s ease-in-out infinite alternate`.

---

```css
.detail-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 20px;
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`align-items: flex-start`: alinea los elementos en el eje transversal con el valor `flex-start`.

`justify-content: space-between`: distribuye los elementos en el eje principal con el valor `space-between`.

`gap: 1rem`: establece la separación entre elementos con el valor `1rem`.

`margin-bottom: 20px`: aplica el margen inferior con el valor `20px`.

---

```css
.detail-title {
  font-family: var(--brand-font);
  font-size: clamp(2rem, 5vw, 3.4rem);
  letter-spacing: .8px;
  text-shadow: 0 12px 28px rgba(0,0,0,.55);
  font-weight: 900;
}
```

`font-family: var(--brand-font)`: aplica la familia tipográfica con el valor `var(--brand-font)`.

`font-size: clamp(2rem, 5vw, 3.4rem)`: establece el tamaño de fuente con el valor `clamp(2rem, 5vw, 3.4rem)`.

`letter-spacing: .8px`: establece la separación entre letras con el valor `.8px`.

`text-shadow: 0 12px 28px rgba(0,0,0,.55)`: aplica una sombra al texto con el valor `0 12px 28px rgba(0,0,0,.55)`.

`font-weight: 900`: establece el grosor tipográfico con el valor `900`.

---

```css
.detail-title .detail-year {
  font-family: var(--font-family-interface);
  font-size: 1.2rem;
  color: var(--color-text-secondary);
  margin-left: .5rem;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`font-size: 1.2rem`: establece el tamaño de fuente con el valor `1.2rem`.

`color: var(--color-text-secondary)`: aplica el color del contenido con el valor `var(--color-text-secondary)`.

`margin-left: .5rem`: aplica el margen izquierdo con el valor `.5rem`.

---

```css
.detail-actions {
  display: flex;
  align-items: center;
  gap: .6rem;
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`align-items: center`: alinea los elementos en el eje transversal con el valor `center`.

`gap: .6rem`: establece la separación entre elementos con el valor `.6rem`.

---

`.detail-card` y su pseudoelemento utilizan ahora la base compartida documentada en `css/components/surfaces.css`. La variante conserva `backdrop-filter: blur(8px) saturate(140%)` y `animation: floatUp .5s ease both`.

---

`.detail-poster`, su imagen y el hover utilizan ahora la base compartida documentada en `css/components/posters.css`. Detail conserva en esta página únicamente `.detail-poster-ph`.

---

```css
.detail-poster-ph {
  aspect-ratio: 2/3;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--color-text-secondary);
  font-size: 1.4rem;
}
```

`aspect-ratio: 2/3`: establece la proporción con el valor `2/3`.

`display: flex`: establece el modelo de presentación con el valor `flex`.

`flex-direction: column`: define la dirección de los elementos flexibles con el valor `column`.

`justify-content: center`: distribuye los elementos en el eje principal con el valor `center`.

`align-items: center`: alinea los elementos en el eje transversal con el valor `center`.

`color: var(--color-text-secondary)`: aplica el color del contenido con el valor `var(--color-text-secondary)`.

`font-size: 1.4rem`: establece el tamaño de fuente con el valor `1.4rem`.

---

```css
.detail-badges .badge {
  font-weight: 700;
  letter-spacing: .3px;
  padding: .45rem .9rem;
  margin-right: .35rem;
  box-shadow: 0 4px 10px rgba(0,0,0,.35);
}
```

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

`letter-spacing: .3px`: establece la separación entre letras con el valor `.3px`.

`padding: .45rem .9rem`: aplica el espacio interior con el valor `.45rem .9rem`.

`margin-right: .35rem`: establece `margin-right` con el valor `.35rem`.

`box-shadow: 0 4px 10px rgba(0,0,0,.35)`: aplica la sombra con el valor `0 4px 10px rgba(0,0,0,.35)`.

---

```css
.detail-section .detail-sub {
  font-family: var(--font-family-interface);
  text-transform: uppercase;
  letter-spacing: .5px;
  color: var(--color-text-secondary);
  font-size: 1rem;
  margin-bottom: .35rem;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`text-transform: uppercase`: transforma visualmente el texto con el valor `uppercase`.

`letter-spacing: .5px`: establece la separación entre letras con el valor `.5px`.

`color: var(--color-text-secondary)`: aplica el color del contenido con el valor `var(--color-text-secondary)`.

`font-size: 1rem`: establece el tamaño de fuente con el valor `1rem`.

`margin-bottom: .35rem`: aplica el margen inferior con el valor `.35rem`.

---

```css
.detail-text {
  font-size: 1.05rem;
  line-height: 1.6;
  color: var(--color-text-primary);
  opacity: .95;
}
```

`font-size: 1.05rem`: establece el tamaño de fuente con el valor `1.05rem`.

`line-height: 1.6`: establece la altura de línea con el valor `1.6`.

`color: var(--color-text-primary)`: aplica el color del contenido con el valor `var(--color-text-primary)`.

`opacity: .95`: establece la opacidad con el valor `.95`.

---

```css
.detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px 20px;
}
```

`display: grid`: establece el modelo de presentación con el valor `grid`.

`grid-template-columns: repeat(auto-fit, minmax(180px, 1fr))`: define las columnas de la cuadrícula con el valor `repeat(auto-fit, minmax(180px, 1fr))`.

`gap: 14px 20px`: establece la separación entre elementos con el valor `14px 20px`.

---

```css
.detail-stat {
  background: rgba(255,255,255,.05);
  border: 1px solid var(--color-border-subtle);
  border-radius: 14px;
  padding: .8rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 2px;
  transition: transform .15s ease, box-shadow .2s ease;
}
```

`background: rgba(255,255,255,.05)`: aplica el fondo con el valor `rgba(255,255,255,.05)`.

`border: 1px solid var(--color-border-subtle)`: aplica el borde con el valor `1px solid var(--color-border-subtle)`.

`border-radius: 14px`: redondea las esquinas con el valor `14px`.

`padding: .8rem 1rem`: aplica el espacio interior con el valor `.8rem 1rem`.

`display: flex`: establece el modelo de presentación con el valor `flex`.

`flex-direction: column`: define la dirección de los elementos flexibles con el valor `column`.

`gap: 2px`: establece la separación entre elementos con el valor `2px`.

`transition: transform .15s ease, box-shadow .2s ease`: suaviza los cambios indicados con el valor `transform .15s ease, box-shadow .2s ease`.

---

```css
.detail-stat:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 22px rgba(0,0,0,.35);
}
```

`transform: translateY(-2px)`: aplica la transformación con el valor `translateY(-2px)`.

`box-shadow: 0 12px 22px rgba(0,0,0,.35)`: aplica la sombra con el valor `0 12px 22px rgba(0,0,0,.35)`.

---

```css
.detail-stat .label {
  font-family: var(--font-family-interface);
  font-size: .85rem;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: .4px;
  font-weight: 700;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`font-size: .85rem`: establece el tamaño de fuente con el valor `.85rem`.

`color: var(--color-text-secondary)`: aplica el color del contenido con el valor `var(--color-text-secondary)`.

`text-transform: uppercase`: transforma visualmente el texto con el valor `uppercase`.

`letter-spacing: .4px`: establece la separación entre letras con el valor `.4px`.

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

---

```css
.detail-stat .value {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--color-text-primary);
}
```

`font-size: 1.2rem`: establece el tamaño de fuente con el valor `1.2rem`.

`font-weight: 800`: establece el grosor tipográfico con el valor `800`.

`color: var(--color-text-primary)`: aplica el color del contenido con el valor `var(--color-text-primary)`.

---

```css
.detail-foot {
  display: flex;
  align-items: center;
  gap: .6rem;
  margin-top: 20px;
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`align-items: center`: alinea los elementos en el eje transversal con el valor `center`.

`gap: .6rem`: establece la separación entre elementos con el valor `.6rem`.

`margin-top: 20px`: aplica el margen superior con el valor `20px`.

---

```css
.detail-actions-spacer {
  height: 56px;
}
```

`height: 56px`: establece la altura con el valor `56px`.


## css/pages/favorites.css

```css
.fav-rail .section-title {
  font-family: var(--font-family-interface);
  letter-spacing: .6px;
  color: var(--color-text-primary);
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`letter-spacing: .6px`: establece la separación entre letras con el valor `.6px`.

`color: var(--color-text-primary)`: aplica el color del contenido con el valor `var(--color-text-primary)`.

---

```css
.rail-badges {
  position: absolute;
  left: .5rem;
  bottom: .5rem;
  display: flex;
  gap: .35rem;
  flex-wrap: wrap;
}
```

`position: absolute`: establece el tipo de posicionamiento con el valor `absolute`.

`left: .5rem`: establece `left` con el valor `.5rem`.

`bottom: .5rem`: establece `bottom` con el valor `.5rem`.

`display: flex`: establece el modelo de presentación con el valor `flex`.

`gap: .35rem`: establece la separación entre elementos con el valor `.35rem`.

`flex-wrap: wrap`: controla el salto de los elementos flexibles con el valor `wrap`.

---

```css
.fav-title {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-family: var(--font-family-interface);
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: .5px;
  color: #fff;
  margin-bottom: 1rem;
  text-transform: uppercase;
  text-shadow: 0 2px 8px rgba(0,0,0,.45);
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`align-items: center`: alinea los elementos en el eje transversal con el valor `center`.

`gap: .5rem`: establece la separación entre elementos con el valor `.5rem`.

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`font-size: 1.6rem`: establece el tamaño de fuente con el valor `1.6rem`.

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

`letter-spacing: .5px`: establece la separación entre letras con el valor `.5px`.

`color: #fff`: aplica el color del contenido con el valor `#fff`.

`margin-bottom: 1rem`: aplica el margen inferior con el valor `1rem`.

`text-transform: uppercase`: transforma visualmente el texto con el valor `uppercase`.

`text-shadow: 0 2px 8px rgba(0,0,0,.45)`: aplica una sombra al texto con el valor `0 2px 8px rgba(0,0,0,.45)`.

---

```css
.fav-title i {
  font-size: 1.4rem;
  color: #9b5cfb;
  filter: drop-shadow(0 0 6px rgba(155,92,251,.5));
}
```

`font-size: 1.4rem`: establece el tamaño de fuente con el valor `1.4rem`.

`color: #9b5cfb`: aplica el color del contenido con el valor `#9b5cfb`.

`filter: drop-shadow(0 0 6px rgba(155,92,251,.5))`: aplica el filtro visual con el valor `drop-shadow(0 0 6px rgba(155,92,251,.5))`.

---

```css
.fav-section .btn-ghost-sm {
  font-family: var(--font-family-interface);
  font-size: 1.2rem;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`font-size: 1.2rem`: establece el tamaño de fuente con el valor `1.2rem`.


## css/pages/groups.css

Las clases `.saga-input` y `.saga-btn` se conservan. `.saga-input` define las dimensiones, el fondo, el borde, el placeholder y el foco específicos del formulario de saga; `.form-control` no reproduce ese resultado. `.saga-btn` conserva una altura, padding, radio, sombra, transición, desplazamiento en hover y comportamiento responsive distintos de los botones compartidos, por lo que sustituirla alteraría el diseño.

```css
.saga-rename {
  background: linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  box-shadow:
    0 8px 26px rgba(10,0,40,.32),
    inset 0 1px 0 rgba(255,255,255,.05);
}
```

`background: linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02))`: aplica el fondo con el valor `linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02))`.

`box-shadow: 0 8px 26px rgba(10,0,40,.32), inset 0 1px 0 rgba(255,255,255,.05)`: aplica la sombra con el valor `0 8px 26px rgba(10,0,40,.32), inset 0 1px 0 rgba(255,255,255,.05)`.

---

```css
.saga-form {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
}
```

`display: grid`: establece el modelo de presentación con el valor `grid`.

`grid-template-columns: 1fr auto`: define las columnas de la cuadrícula con el valor `1fr auto`.

`gap: 12px`: establece la separación entre elementos con el valor `12px`.

---

```css
.saga-input {
  display: block;
  width: 100%;
  height: 56px;
  border-radius: 14px;
  border: 1px solid var(--color-border-subtle);
  background: rgba(255,255,255,.05);
  color: var(--color-text-primary);
  padding: 0 16px;
  font-family: var(--font-family-body);
  font-size: 1rem;
  line-height: 1;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.05);
}
```

`display: block`: establece el modelo de presentación con el valor `block`.

`width: 100%`: establece el ancho con el valor `100%`.

`height: 56px`: establece la altura con el valor `56px`.

`border-radius: 14px`: redondea las esquinas con el valor `14px`.

`border: 1px solid var(--color-border-subtle)`: aplica el borde con el valor `1px solid var(--color-border-subtle)`.

`background: rgba(255,255,255,.05)`: aplica el fondo con el valor `rgba(255,255,255,.05)`.

`color: var(--color-text-primary)`: aplica el color del contenido con el valor `var(--color-text-primary)`.

`padding: 0 16px`: aplica el espacio interior con el valor `0 16px`.

`font-family: var(--font-family-body)`: aplica la familia tipográfica con el valor `var(--font-family-body)`.

`font-size: 1rem`: establece el tamaño de fuente con el valor `1rem`.

`line-height: 1`: establece la altura de línea con el valor `1`.

`box-shadow: inset 0 0 0 1px rgba(255,255,255,.05)`: aplica la sombra con el valor `inset 0 0 0 1px rgba(255,255,255,.05)`.

---

```css
.saga-input::placeholder {
  color: rgba(255,255,255,.55);
}
```

`color: rgba(255,255,255,.55)`: aplica el color del contenido con el valor `rgba(255,255,255,.55)`.

---

```css
.saga-input:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(155,92,251,.35);
}
```

`outline: none`: aplica el contorno con el valor `none`.

`box-shadow: 0 0 0 2px rgba(155,92,251,.35)`: aplica la sombra con el valor `0 0 0 2px rgba(155,92,251,.35)`.

---

```css
.saga-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  padding: 0 1.35rem;
  border-radius: 14px;
  border: none;
  background: linear-gradient(135deg,var(--accent),var(--color-accent-dark));
  color: #fff;
  font-family: var(--font-family-body);
  font-weight: 800;
  line-height: 1;
  box-shadow:
    0 14px 34px rgba(111,63,230,.45),
    inset 0 0 0 1px rgba(255,255,255,.08);
  transition: transform .15s ease,filter .2s ease;
}
```

`display: inline-flex`: establece el modelo de presentación con el valor `inline-flex`.

`align-items: center`: alinea los elementos en el eje transversal con el valor `center`.

`justify-content: center`: distribuye los elementos en el eje principal con el valor `center`.

`height: 56px`: establece la altura con el valor `56px`.

`padding: 0 1.35rem`: aplica el espacio interior con el valor `0 1.35rem`.

`border-radius: 14px`: redondea las esquinas con el valor `14px`.

`border: none`: aplica el borde con el valor `none`.

`background: linear-gradient(135deg,var(--accent),var(--color-accent-dark))`: aplica el fondo con el valor `linear-gradient(135deg,var(--accent),var(--color-accent-dark))`.

`color: #fff`: aplica el color del contenido con el valor `#fff`.

`font-family: var(--font-family-body)`: aplica la familia tipográfica con el valor `var(--font-family-body)`.

`font-weight: 800`: establece el grosor tipográfico con el valor `800`.

`line-height: 1`: establece la altura de línea con el valor `1`.

`box-shadow: 0 14px 34px rgba(111,63,230,.45), inset 0 0 0 1px rgba(255,255,255,.08)`: aplica la sombra con el valor `0 14px 34px rgba(111,63,230,.45), inset 0 0 0 1px rgba(255,255,255,.08)`.

`transition: transform .15s ease,filter .2s ease`: suaviza los cambios indicados con el valor `transform .15s ease,filter .2s ease`.

---

```css
.saga-btn:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
}
```

`transform: translateY(-2px)`: aplica la transformación con el valor `translateY(-2px)`.

`filter: brightness(1.06)`: aplica el filtro visual con el valor `brightness(1.06)`.

---

```css
@media (max-width: 720px) {
  .saga-form {
    grid-template-columns: 1fr;
  }
  .saga-btn {
    width: 100%;
  }
}
```

`@media (max-width: 720px)`: aplica las reglas internas únicamente cuando se cumple esta condición de ancho de pantalla.

`.saga-form`: define las columnas de la cuadrícula con el valor `1fr`.

`.saga-btn`: establece el ancho con el valor `100%`.


```css

---

```css
.edit-card input[name="volveria_a_ver"].form-check-input:checked {
  background-color: #1e90ff;
  border-color: rgba(0,0,0,.15);
}
```

`background-color: #1e90ff`: aplica el color de fondo `#1e90ff`.

`border-color: rgba(0,0,0,.15)`: establece el color del borde en `rgba(0,0,0,.15)`.

---

```css
.edit-card input[name="tendra_continuacion"].form-check-input:checked {
  background-color: #2ecc71;
  border-color: rgba(0,0,0,.15);
}
```

`background-color: #2ecc71`: aplica el color de fondo `#2ecc71`.

`border-color: rgba(0,0,0,.15)`: establece el color del borde en `rgba(0,0,0,.15)`.

## css/pages/marathons.css

```css
.selectable-card {
  cursor: pointer;
  border-radius: 12px;
  transition: all 0.2s ease;
}
```

`cursor: pointer`: establece la apariencia del cursor con el valor `pointer`.

`border-radius: 12px`: redondea las esquinas con el valor `12px`.

`transition: all 0.2s ease`: suaviza los cambios indicados con el valor `all 0.2s ease`.

---

```css
.selectable-card.selected {
  box-shadow: 0 0 12px 3px rgba(180, 70, 255, 0.7);
  transform: scale(1.02);
}
```

`box-shadow: 0 0 12px 3px rgba(180, 70, 255, 0.7)`: aplica la sombra con el valor `0 0 12px 3px rgba(180, 70, 255, 0.7)`.

`transform: scale(1.02)`: aplica la transformación con el valor `scale(1.02)`.

---

```css
.mara-card {
  overflow: hidden
}
```

`overflow: hidden`: controla el contenido desbordado con el valor `hidden`.

---

```css
.mara-card > .mara-cover {
  position: relative;
  height: 160px;
  overflow: visible;
}
```

`position: relative`: establece el tipo de posicionamiento con el valor `relative`.

`height: 160px`: establece la altura con el valor `160px`.

`overflow: visible`: controla el contenido desbordado con el valor `visible`.

---

```css
.mara-card > .mara-cover::before {
  content: "";
  position: absolute;
  inset: -24px;
  background-image: var(--m-bg);
  background-size: cover;
  background-position: center;
  filter: blur(20px);
  transform: scale(1.12);
  z-index: 0;
  pointer-events: none;
}
```

`content: ""`: define el contenido generado con el valor `""`.

`position: absolute`: establece el tipo de posicionamiento con el valor `absolute`.

`inset: -24px`: sitúa los cuatro bordes con el valor `-24px`.

`background-image: var(--m-bg)`: aplica la imagen de fondo con el valor `var(--m-bg)`.

`background-size: cover`: define el tamaño del fondo con el valor `cover`.

`background-position: center`: sitúa el fondo con el valor `center`.

`filter: blur(20px)`: aplica el filtro visual con el valor `blur(20px)`.

`transform: scale(1.12)`: aplica la transformación con el valor `scale(1.12)`.

`z-index: 0`: establece el nivel de apilamiento con el valor `0`.

`pointer-events: none`: controla la interacción del puntero con el valor `none`.

---

```css
.mara-card .mara-preview {
  position: absolute;
  left: 14px;
  right: 14px;
  bottom: -28px;
  display: flex;
  gap: 10px;
  overflow: visible;
  z-index: 2;
}
```

`position: absolute`: establece el tipo de posicionamiento con el valor `absolute`.

`left: 14px`: sitúa el borde izquierdo con el valor `14px`.

`right: 14px`: sitúa el borde derecho con el valor `14px`.

`bottom: -28px`: sitúa el borde inferior con el valor `-28px`.

`display: flex`: establece el modelo de presentación con el valor `flex`.

`gap: 10px`: establece la separación entre elementos con el valor `10px`.

`overflow: visible`: controla el contenido desbordado con el valor `visible`.

`z-index: 2`: establece el nivel de apilamiento con el valor `2`.

---

```css
.mara-card .mara-thumb {
  width: 70px;
  aspect-ratio: 2/3;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 18px rgba(0,0,0,.35);
  flex: 0 0 auto;
}
```

`width: 70px`: establece el ancho con el valor `70px`.

`aspect-ratio: 2/3`: establece la proporción con el valor `2/3`.

`border-radius: 12px`: redondea las esquinas con el valor `12px`.

`overflow: hidden`: controla el contenido desbordado con el valor `hidden`.

`box-shadow: 0 6px 18px rgba(0,0,0,.35)`: aplica la sombra con el valor `0 6px 18px rgba(0,0,0,.35)`.

`flex: 0 0 auto`: configura el comportamiento flexible con el valor `0 0 auto`.

---

```css
.mara-card .mara-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block
}
```

`width: 100%`: establece el ancho con el valor `100%`.

`height: 100%`: establece la altura con el valor `100%`.

`object-fit: cover`: ajusta la imagen dentro de su caja con el valor `cover`.

`display: block`: establece el modelo de presentación con el valor `block`.

---

```css
.mara-body {
  margin-top: 28px;
  display: grid;
  grid-template-columns: 1fr auto;
  column-gap: 1.25rem;
  align-items: start;
}
```

`margin-top: 28px`: aplica el margen superior con el valor `28px`.

`display: grid`: establece el modelo de presentación con el valor `grid`.

`grid-template-columns: 1fr auto`: define las columnas de la cuadrícula con el valor `1fr auto`.

`column-gap: 1.25rem`: separa las columnas con el valor `1.25rem`.

`align-items: start`: alinea los elementos transversalmente con el valor `start`.

---

```css
.mara-side {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: .65rem
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`flex-direction: column`: define la dirección flexible con el valor `column`.

`align-items: flex-end`: alinea los elementos transversalmente con el valor `flex-end`.

`gap: .65rem`: establece la separación entre elementos con el valor `.65rem`.

---

```css
.mara-side .actions {
  display: flex;
  gap: .5rem
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`gap: .5rem`: establece la separación entre elementos con el valor `.5rem`.

---

```css
.mara-title {
  font-family: var(--font-family-interface);
  line-height: 1.1;
  letter-spacing: .3px;
}
```

`font-family: var(--font-family-interface)`: aplica la familia tipográfica con el valor `var(--font-family-interface)`.

`line-height: 1.1`: establece la altura de línea con el valor `1.1`.

`letter-spacing: .3px`: separa las letras con el valor `.3px`.

---

```css
.mara-title a {
  color: inherit;
  text-decoration: none;
}
```

`color: inherit`: aplica el color del contenido con el valor `inherit`.

`text-decoration: none`: aplica la decoración del texto con el valor `none`.

---

```css
.mara-title a:hover {
  color: #fff;
}
```

`color: #fff`: aplica el color del contenido con el valor `#fff`.

---

```css
.mara-chip {
  background: rgba(180,70,255,.18);
  border: 1px solid rgba(180,70,255,.35)
}
```

`background: rgba(180,70,255,.18)`: aplica el fondo con el valor `rgba(180,70,255,.18)`.

`border: 1px solid rgba(180,70,255,.35)`: aplica el borde con el valor `1px solid rgba(180,70,255,.35)`.

---

```css
@media (max-width: 768px) {
  .mara-body {
    grid-template-columns: 1fr;
    row-gap: .75rem
  }
  .mara-side {
    align-items: flex-end
  }
}
```

`@media (max-width: 768px)`: aplica las reglas internas únicamente cuando se cumple esta condición de ancho de pantalla.

`.mara-body`: define las columnas de la cuadrícula con el valor `1fr`. separa las filas con el valor `.75rem`.

`.mara-side`: alinea los elementos transversalmente con el valor `flex-end`.

---

```css
@media (max-width: 576px) {
  .mara-card > .mara-cover {
    height: 120px
  }
  .mara-card .mara-thumb {
    width: 56px
  }
}
```

`@media (max-width: 576px)`: aplica las reglas internas únicamente cuando se cumple esta condición de ancho de pantalla.

`.mara-card > .mara-cover`: establece la altura con el valor `120px`.

`.mara-card .mara-thumb`: establece el ancho con el valor `56px`.

---

```css
.maraton-form-actions-sticky {
  position: sticky;
  top: 110px;
  z-index: 20;

  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;

  margin-bottom: 1rem;
  padding: 0.85rem 1rem;

  background:
    linear-gradient(
      135deg,
      rgba(44, 22, 73, 0.96),
      rgba(26, 27, 68, 0.96)
    );

  border: 1px solid rgba(177, 119, 255, 0.32);
  border-radius: 16px;

  box-shadow:
    0 12px 28px rgba(0, 0, 0, 0.28),
    0 0 18px rgba(129, 69, 220, 0.12);

  backdrop-filter: blur(12px);
}
```

`position: sticky`: establece el tipo de posicionamiento con el valor `sticky`.

`top: 110px`: sitúa el borde superior con el valor `110px`.

`z-index: 20`: establece el nivel de apilamiento con el valor `20`.

`display: flex`: establece el modelo de presentación con el valor `flex`.

`align-items: center`: alinea los elementos transversalmente con el valor `center`.

`justify-content: space-between`: distribuye los elementos en el eje principal con el valor `space-between`.

`gap: 1rem`: establece la separación entre elementos con el valor `1rem`.

`margin-bottom: 1rem`: aplica el margen inferior con el valor `1rem`.

`padding: 0.85rem 1rem`: aplica el espacio interior con el valor `0.85rem 1rem`.

`background: linear-gradient( 135deg, rgba(44, 22, 73, 0.96), rgba(26, 27, 68, 0.96) )`: aplica el fondo con el valor `linear-gradient( 135deg, rgba(44, 22, 73, 0.96), rgba(26, 27, 68, 0.96) )`.

`border: 1px solid rgba(177, 119, 255, 0.32)`: aplica el borde con el valor `1px solid rgba(177, 119, 255, 0.32)`.

`border-radius: 16px`: redondea las esquinas con el valor `16px`.

`box-shadow: 0 12px 28px rgba(0, 0, 0, 0.28), 0 0 18px rgba(129, 69, 220, 0.12)`: aplica la sombra con el valor `0 12px 28px rgba(0, 0, 0, 0.28), 0 0 18px rgba(129, 69, 220, 0.12)`.

`backdrop-filter: blur(12px)`: filtra el contenido situado detrás con el valor `blur(12px)`.

---

```css
.maraton-selection-count {
  color: rgba(245, 241, 255, 0.82);
  font-weight: 600;
}
```

`color: rgba(245, 241, 255, 0.82)`: aplica el color del contenido con el valor `rgba(245, 241, 255, 0.82)`.

`font-weight: 600`: establece el grosor tipográfico con el valor `600`.

---

```css
#filtro-mara::-webkit-input-placeholder {
  color: rgba(246,243,255,.8);
}
```

`color: rgba(246,243,255,.8)`: aplica el color del contenido con el valor `rgba(246,243,255,.8)`.

---

```css
#filtro-mara::-moz-placeholder {
  color: rgba(246,243,255,.8);
  opacity: 1;
}
```

`color: rgba(246,243,255,.8)`: aplica el color del contenido con el valor `rgba(246,243,255,.8)`.

`opacity: 1`: establece la opacidad con el valor `1`.

---

```css
#filtro-mara::placeholder {
  color: rgba(246,243,255,.8);
}
```

`color: rgba(246,243,255,.8)`: aplica el color del contenido con el valor `rgba(246,243,255,.8)`.


## css/pages/pending.css

```css
.nav.nav-pills {
  gap: .5rem;
}
```

`gap: .5rem`: establece la separación entre elementos con el valor `.5rem`.

---

```css
.nav-pills .nav-link {
  color: var(--color-text-secondary);
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.10);
  border-radius: 12px;
  padding: .5rem .9rem;
  font-family: var(--font-family-body);
  font-weight: 700;
}
```

`color: var(--color-text-secondary)`: aplica el color del contenido con el valor `var(--color-text-secondary)`.

`background: rgba(255,255,255,.04)`: aplica el fondo con el valor `rgba(255,255,255,.04)`.

`border: 1px solid rgba(255,255,255,.10)`: aplica el borde con el valor `1px solid rgba(255,255,255,.10)`.

`border-radius: 12px`: redondea las esquinas con el valor `12px`.

`padding: .5rem .9rem`: aplica el espacio interior con el valor `.5rem .9rem`.

`font-family: var(--font-family-body)`: aplica la familia tipográfica con el valor `var(--font-family-body)`.

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

---

```css
.nav-pills .nav-link:hover {
  color: var(--color-text-primary);
  background: rgba(255,255,255,.06);
  border-color: rgba(255,255,255,.18);
}
```

`color: var(--color-text-primary)`: aplica el color del contenido con el valor `var(--color-text-primary)`.

`background: rgba(255,255,255,.06)`: aplica el fondo con el valor `rgba(255,255,255,.06)`.

`border-color: rgba(255,255,255,.18)`: aplica el color del borde con el valor `rgba(255,255,255,.18)`.

---

```css
.nav-pills .nav-link.active {
  color: #fff;
  background: radial-gradient(120% 120% at 20% 0%,
              rgba(180,120,255,.35) 0%,
              rgba(120,70,255,.24) 45%,
              rgba(120,70,255,.16) 100%);
  border-color: rgba(190,150,255,.6);
  box-shadow: 0 10px 24px rgba(120,70,255,.3), inset 0 1px 0 rgba(255,255,255,.14);
}
```

`color: #fff`: aplica el color del contenido con el valor `#fff`.

`background: radial-gradient(120% 120% at 20% 0%, rgba(180,120,255,.35) 0%, rgba(120,70,255,.24) 45%, rgba(120,70,255,.16) 100%)`: aplica el fondo con el valor `radial-gradient(120% 120% at 20% 0%, rgba(180,120,255,.35) 0%, rgba(120,70,255,.24) 45%, rgba(120,70,255,.16) 100%)`.

`border-color: rgba(190,150,255,.6)`: aplica el color del borde con el valor `rgba(190,150,255,.6)`.

`box-shadow: 0 10px 24px rgba(120,70,255,.3), inset 0 1px 0 rgba(255,255,255,.14)`: aplica la sombra con el valor `0 10px 24px rgba(120,70,255,.3), inset 0 1px 0 rgba(255,255,255,.14)`.

---

```css
.kanban-col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-height: 140px;
  overflow-y: auto;
  padding: .25rem 0 .25rem;
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`flex-direction: column`: define la dirección flexible con el valor `column`.

`gap: 1rem`: establece la separación entre elementos con el valor `1rem`.

`min-height: 140px`: establece la altura mínima con el valor `140px`.

`overflow-y: auto`: controla el desbordamiento vertical con el valor `auto`.

`padding: .25rem 0 .25rem`: aplica el espacio interior con el valor `.25rem 0 .25rem`.

---

```css
.kan-empty {
  color: rgba(255,255,255,.65);
  font-size: .92rem;
  padding: .35rem .5rem;
}
```

`color: rgba(255,255,255,.65)`: aplica el color del contenido con el valor `rgba(255,255,255,.65)`.

`font-size: .92rem`: establece el tamaño de fuente con el valor `.92rem`.

`padding: .35rem .5rem`: aplica el espacio interior con el valor `.35rem .5rem`.

---

```css
.kanban-col.col-dragover {
  outline: 2px dashed rgba(190,150,255,.45);
  outline-offset: 6px;
  border-radius: 16px;
  background: linear-gradient(180deg, rgba(150,110,255,.10), rgba(150,110,255,.04));
}
```

`outline: 2px dashed rgba(190,150,255,.45)`: aplica el contorno con el valor `2px dashed rgba(190,150,255,.45)`.

`outline-offset: 6px`: desplaza el contorno con el valor `6px`.

`border-radius: 16px`: redondea las esquinas con el valor `16px`.

`background: linear-gradient(180deg, rgba(150,110,255,.10), rgba(150,110,255,.04))`: aplica el fondo con el valor `linear-gradient(180deg, rgba(150,110,255,.10), rgba(150,110,255,.04))`.

---

```css
.kan-item {
  position: relative;
  width: 100%;
}
```

`position: relative`: establece el tipo de posicionamiento con el valor `relative`.

`width: 100%`: establece el ancho con el valor `100%`.

---

```css
.kan-poster {
  display: block;
  border-radius: 16px;
  overflow: hidden;
}
```

`display: block`: establece el modelo de presentación con el valor `block`.

`border-radius: 16px`: redondea las esquinas con el valor `16px`.

`overflow: hidden`: controla el contenido desbordado con el valor `hidden`.

---

```css
.kan-poster:hover img {
  transform: translateY(-2px);
  box-shadow: 0 14px 30px rgba(10,0,40,.36);
}
```

`transform: translateY(-2px)`: aplica la transformación con el valor `translateY(-2px)`.

`box-shadow: 0 14px 30px rgba(10,0,40,.36)`: aplica la sombra con el valor `0 14px 30px rgba(10,0,40,.36)`.

---

```css
.kan-badges {
  position: absolute;
  left: .6rem;
  bottom: .6rem;
  display: flex;
  gap: .35rem;
  flex-wrap: wrap;
}
```

`position: absolute`: establece el tipo de posicionamiento con el valor `absolute`.

`left: .6rem`: sitúa el borde izquierdo con el valor `.6rem`.

`bottom: .6rem`: sitúa el borde inferior con el valor `.6rem`.

`display: flex`: establece el modelo de presentación con el valor `flex`.

`gap: .35rem`: establece la separación entre elementos con el valor `.35rem`.

`flex-wrap: wrap`: controla el salto de elementos con el valor `wrap`.

---

```css
.focus-list .focus-row {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .45rem .6rem;
  border-radius: 12px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.08);
}
```

`display: flex`: establece el modelo de presentación con el valor `flex`.

`align-items: center`: alinea los elementos transversalmente con el valor `center`.

`gap: .75rem`: establece la separación entre elementos con el valor `.75rem`.

`padding: .45rem .6rem`: aplica el espacio interior con el valor `.45rem .6rem`.

`border-radius: 12px`: redondea las esquinas con el valor `12px`.

`background: rgba(255,255,255,.03)`: aplica el fondo con el valor `rgba(255,255,255,.03)`.

`border: 1px solid rgba(255,255,255,.08)`: aplica el borde con el valor `1px solid rgba(255,255,255,.08)`.

---

```css
.focus-list .focus-row + .focus-row {
  margin-top: .5rem;
}
```

`margin-top: .5rem`: aplica el margen superior con el valor `.5rem`.

---

```css
.focus-list .poster {
  width: 48px;
  border-radius: 10px;
  overflow: hidden;
  flex-shrink: 0;
  box-shadow: 0 6px 16px rgba(10,0,40,.28);
}
```

`width: 48px`: establece el ancho con el valor `48px`.

`border-radius: 10px`: redondea las esquinas con el valor `10px`.

`overflow: hidden`: controla el contenido desbordado con el valor `hidden`.

`flex-shrink: 0`: controla la reducción flexible con el valor `0`.

`box-shadow: 0 6px 16px rgba(10,0,40,.28)`: aplica la sombra con el valor `0 6px 16px rgba(10,0,40,.28)`.

---

```css
.focus-list .title {
  font-weight: 700;
  line-height: 1.2;
}
```

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

`line-height: 1.2`: establece la altura de línea con el valor `1.2`.

---

```css
.focus-list .meta {
  opacity: .75;
  font-size: .85rem;
}
```

`opacity: .75`: establece la opacidad con el valor `.75`.

`font-size: .85rem`: establece el tamaño de fuente con el valor `.85rem`.

---

```css
.tile {
  background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02));
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 18px;
  box-shadow: 0 8px 26px rgba(10,0,40,.32), inset 0 1px 0 rgba(255,255,255,.05);
}
```

`background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02))`: aplica el fondo con el valor `linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02))`.

`border: 1px solid rgba(255,255,255,.12)`: aplica el borde con el valor `1px solid rgba(255,255,255,.12)`.

`border-radius: 18px`: redondea las esquinas con el valor `18px`.

`box-shadow: 0 8px 26px rgba(10,0,40,.32), inset 0 1px 0 rgba(255,255,255,.05)`: aplica la sombra con el valor `0 8px 26px rgba(10,0,40,.32), inset 0 1px 0 rgba(255,255,255,.05)`.

---

```css
.tile .tile-header {
  font-family: var(--brand-font);
  letter-spacing: .6px;
  color: var(--color-text-primary);
}
```

`font-family: var(--brand-font)`: aplica la familia tipográfica con el valor `var(--brand-font)`.

`letter-spacing: .6px`: separa las letras con el valor `.6px`.

`color: var(--color-text-primary)`: aplica el color del contenido con el valor `var(--color-text-primary)`.

---

```css
.kan-poster-small {
  width: 40px;
  flex-shrink: 0;
}
```

`width: 40px`: establece el ancho con el valor `40px`.

`flex-shrink: 0`: controla la reducción flexible con el valor `0`.


## css/pages/rewatch.css

```css
.rewatch-badge {
  background: #1e90ff;
  color: #fff;
  font-weight: 700;
  box-shadow: 0 6px 16px rgba(30,144,255,.35);
}
```

`background: #1e90ff`: aplica el fondo con el valor `#1e90ff`.

`color: #fff`: aplica el color del contenido con el valor `#fff`.

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

`box-shadow: 0 6px 16px rgba(30,144,255,.35)`: aplica la sombra con el valor `0 6px 16px rgba(30,144,255,.35)`.

---

```css
.rew-grid-7x2 {
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  grid-auto-rows: 1fr;
  gap: 16px;
}
```

`display: grid`: establece el modelo de presentación con el valor `grid`.

`grid-template-columns: repeat(7, minmax(0, 1fr))`: define las columnas de la cuadrícula con el valor `repeat(7, minmax(0, 1fr))`.

`grid-auto-rows: 1fr`: define el tamaño de filas automáticas con el valor `1fr`.

`gap: 16px`: establece la separación entre elementos con el valor `16px`.

---

```css
.rew-grid-7x2 .rail-card {
  width: 100%;
  height: 100%;
}
```

`width: 100%`: establece el ancho con el valor `100%`.

`height: 100%`: establece la altura con el valor `100%`.

---

```css
.rew-grid-7x2 .rail-poster {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: inherit;
}
```

`width: 100%`: establece el ancho con el valor `100%`.

`height: 100%`: establece la altura con el valor `100%`.

`display: block`: establece el modelo de presentación con el valor `block`.

`border-radius: inherit`: redondea las esquinas con el valor `inherit`.

---

```css
.rew-grid-7x2 .rail-poster img.rew-fit {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: inherit;
  background: rgba(0,0,0,.22);
}
```

`width: 100%`: establece el ancho con el valor `100%`.

`height: 100%`: establece la altura con el valor `100%`.

`object-fit: contain`: ajusta la imagen dentro de su caja con el valor `contain`.

`border-radius: inherit`: redondea las esquinas con el valor `inherit`.

`background: rgba(0,0,0,.22)`: aplica el fondo con el valor `rgba(0,0,0,.22)`.
