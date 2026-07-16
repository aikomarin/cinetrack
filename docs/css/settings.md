## css/settings/tokens.css

```css
:root {
  /* Tipografía: Fuentes de la aplicación */
  --brand-font: 'Bebas Neue', system-ui, sans-serif;
  --ui-font: 'Teko', system-ui, sans-serif;
  --text-font: 'DM Sans', system-ui, sans-serif;

  /* Base: Colores generales */
  --bg-0: #0b0712;
  --bg-1: #120a1f;
  --bg-2: #1a1030;
  --ink: #f6f3ff;
  --ink-dim: #dcd3fb;
  --accent: #9b5cfb;
  --accent-2: #6f3fe6;
  --accent-3: #14ffe9;
  --line: rgba(255,255,255,.12);

  /* Layout: Espaciado de los rollos laterales */
  --rail-w: 140px;
  --rails-pad: calc(var(--rail-w) + 18px);

  /* Componente: Colores de la claqueta */
  --clap-body: #7c3aed;
  --clap-body-dark: #5b2bb5;
  --clap-stripe: #ffffff;
  --clap-edge: rgba(0,0,0,.28);

  /* Layout: Animación de las perforaciones de película */
  --sprocket-speed: 1s;
  --sprocket-step: 66px;
  --sprocket-hole: 30px;
}
```

`:root`: hace que las variables declaradas dentro del bloque estén disponibles para todo el documento.

`/* Tipografía: Fuentes de la aplicación */`: identifica el grupo de fuentes utilizado por la marca, la interfaz y el texto general.

`--brand-font: 'Bebas Neue', system-ui, sans-serif`: contiene Bebas Neue como fuente principal, con fuentes sans serif de respaldo. Se utiliza para textos de marca y títulos destacados con letras altas y condensadas. El nombre indica con claridad que corresponde a la tipografía de marca.

`--ui-font: 'Teko', system-ui, sans-serif`: contiene Teko como fuente principal, con fuentes sans serif de respaldo. Se utiliza en títulos de interfaz, navegación, labels y controles que necesitan una apariencia condensada. La abreviatura `ui` significa “interfaz de usuario”, pero puede no ser evidente para quien no conozca el término.

Pendiente de nomenclatura: `--ui-font` utiliza una abreviatura técnica. No se modifica todavía porque tiene dependencias en numerosos componentes.

`--text-font: 'DM Sans', system-ui, sans-serif`: contiene DM Sans como fuente principal de lectura, con fuentes sans serif de respaldo. Se utiliza como tipografía general del cuerpo y de textos corrientes.

Pendiente de nomenclatura: `--text-font` indica que es una fuente de texto, pero no deja claro que funciona como tipografía general de lectura. No se modifica todavía porque tiene dependencias en varios archivos.

`/* Base: Colores generales */`: identifica el grupo de colores oscuros, colores de texto, acentos y bordes compartidos.

`--bg-0: #0b0712`: contiene un violeta casi negro. Parece representar el nivel más oscuro de la escala de fondos. El nombre `bg` abrevia “background” y el número `0` no explica por sí solo dónde debe utilizarse.

Pendiente de nomenclatura: `--bg-0` utiliza una escala numérica poco descriptiva. No se modifica todavía hasta revisar todos sus usos.

`--bg-1: #120a1f`: contiene un violeta oscuro. Parece representar un segundo nivel de fondo, ligeramente más claro que `--bg-0`. El número `1` expresa una posición en la escala, pero no una responsabilidad visual concreta.

Pendiente de nomenclatura: `--bg-1` necesita revisarse junto con el resto de fondos antes de definir un nombre más semántico.

`--bg-2: #1a1030`: contiene un morado oscuro más visible. Se utiliza como fondo de superficies elevadas, actualmente en el menú del select personalizado. El número `2` no explica que funciona como color de panel o superficie.

Pendiente de nomenclatura: `--bg-2` necesita revisarse junto con sus consumidores antes de renombrarse.

`--ink: #f6f3ff`: contiene un blanco muy claro con un matiz violeta. Funciona como color principal del texto sobre los fondos oscuros.

Pendiente de nomenclatura: `--ink` significa “tinta”, pero no indica claramente que representa el color principal del texto. No se modifica todavía porque tiene dependencias en varios archivos.

`--ink-dim: #dcd3fb`: contiene un lavanda muy claro, algo más apagado que `--ink`. Se utiliza para subtítulos, metadatos y texto con menor énfasis visual.

Pendiente de nomenclatura: `--ink-dim` relaciona el color con `--ink`, pero `dim` es una abreviatura inglesa que no explica directamente que representa texto secundario.

`--accent: #9b5cfb`: contiene un morado luminoso. Funciona como color de acento principal en botones, barras, navegación, bordes activos y elementos destacados. El nombre es comprensible, aunque no indica que es el acento principal.

`--accent-2: #6f3fe6`: contiene un morado más oscuro. Se utiliza junto con `--accent` para completar degradados y variaciones del color principal. El número `2` expresa que es una segunda variante, pero no su función exacta.

Pendiente de nomenclatura: `--accent-2` debe revisarse junto con toda la familia de acentos antes de asignarle un nombre más descriptivo.

`--accent-3: #14ffe9`: contiene un cian neón brillante. Está definido como tercer color de acento, aunque su nombre no especifica qué tipo de elementos debería destacar.

Pendiente de nomenclatura: `--accent-3` necesita revisar sus usos reales antes de decidir si representa un acento funcional o una variante cromática.

`--line: rgba(255,255,255,.12)`: contiene blanco con una opacidad del 12 %. Se utiliza para crear bordes y líneas muy sutiles sobre superficies oscuras. El nombre es corto y comprensible dentro del CSS, aunque no indica expresamente que representa un borde translúcido.

Pendiente de nomenclatura: `--line` podría necesitar un nombre más específico si en el futuro existen varios tipos de bordes o separadores.

`/* Layout: Espaciado de los rollos laterales */`: identifica las variables que reservan espacio para los rollos de película situados a los lados de la interfaz.

`--rail-w: 140px`: establece en 140 píxeles el ancho base de cada rollo lateral. `w` abrevia “width”, por lo que el nombre puede no ser evidente sin conocer el componente.

Pendiente de nomenclatura: `--rail-w` contiene una abreviatura y debe revisarse cuando se trabaje el responsive de los rollos laterales.

`--rails-pad: calc(var(--rail-w) + 18px)`: calcula el espacio lateral reservado para el contenido sumando 18 píxeles al ancho del rollo. Esto evita que el contenido principal quede debajo de los rollos. `pad` abrevia “padding”.

Pendiente de nomenclatura: `--rails-pad` utiliza una abreviatura y depende directamente de `--rail-w`; ambas variables deben revisarse juntas.

`/* Componente: Colores de la claqueta */`: identifica los colores compartidos por los elementos visuales con forma de claqueta.

`--clap-body: #7c3aed`: contiene el morado principal del cuerpo de la claqueta. `clap` es una abreviación de “clapboard” y puede no resultar clara fuera del contexto del componente.

Pendiente de nomenclatura: las variables `--clap-*` deben revisarse como una familia completa antes de renombrarse.

`--clap-body-dark: #5b2bb5`: contiene un morado más oscuro utilizado para completar el degradado del cuerpo de la claqueta.

`--clap-stripe: #ffffff`: contiene blanco puro y se utiliza en las franjas claras de la tapa de la claqueta.

`--clap-edge: rgba(0,0,0,.28)`: contiene negro con una opacidad del 28 %. Se utiliza para marcar bordes, sombras interiores y remaches de la claqueta.

`/* Layout: Animación de las perforaciones de película */`: identifica las medidas y la velocidad utilizadas por el patrón animado de perforaciones de los rollos laterales.

`--sprocket-speed: 1s`: establece en un segundo la duración de cada ciclo de movimiento del patrón de perforaciones.

`--sprocket-step: 66px`: establece en 66 píxeles la altura completa de cada repetición del patrón, incluyendo la perforación y el espacio vacío.

`--sprocket-hole: 30px`: establece en 30 píxeles la parte visible de cada perforación dentro del patrón repetido.
