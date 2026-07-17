## css/settings/tokens.css

```css
:root {
  /* Tipografía: Fuentes de la aplicación */
  --brand-font: 'Bebas Neue', system-ui, sans-serif;
  --font-family-interface: 'Teko', system-ui, sans-serif;
  --font-family-body: 'DM Sans', system-ui, sans-serif;

  /* Base: Colores generales */
  --color-surface-base: #120a1f;
  --color-surface-elevated: #1a1030;
  --color-text-primary: #f6f3ff;
  --color-text-secondary: #dcd3fb;
  --accent: #9b5cfb;
  --color-accent-dark: #6f3fe6;
  --color-border-subtle: rgba(255,255,255,.12);
}
```

`:root`: hace que las variables declaradas dentro del bloque estén disponibles para todo el documento.

`--brand-font: 'Bebas Neue', system-ui, sans-serif`: contiene Bebas Neue como fuente principal, con fuentes sans serif de respaldo. Se utiliza para textos de marca y títulos destacados con letras altas y condensadas. El nombre indica con claridad que corresponde a la tipografía de marca.

`--font-family-interface: 'Teko', system-ui, sans-serif`: contiene Teko como fuente principal, con fuentes sans serif de respaldo. Se utiliza en títulos de interfaz, navegación, labels y controles que necesitan una apariencia condensada. La abreviatura `ui` significa “interfaz de usuario”, pero puede no ser evidente para quien no conozca el término.

`--font-family-body: 'DM Sans', system-ui, sans-serif`: contiene DM Sans como fuente principal de lectura, con fuentes sans serif de respaldo. Se utiliza como tipografía general del cuerpo y de textos corrientes.

`--color-surface-base: #120a1f`: contiene el nivel base de una superficie oscura. Se utiliza como extremo inferior del degradado del menú del selector personalizado.

`--color-surface-elevated: #1a1030`: contiene un morado oscuro más visible. Se utiliza como fondo de superficies elevadas, actualmente en el menú del select personalizado. El número `2` no explica que funciona como color de panel o superficie.

`--color-text-primary: #f6f3ff`: contiene un blanco muy claro con un matiz violeta. Funciona como color principal del texto sobre los fondos oscuros.

`--color-text-secondary: #dcd3fb`: contiene un lavanda muy claro, algo más apagado que `--color-text-primary`. Se utiliza para subtítulos, metadatos y texto con menor énfasis visual.

`--accent: #9b5cfb`: contiene un morado luminoso. Funciona como color de acento principal en botones, barras, navegación, bordes activos y elementos destacados. El nombre es comprensible, aunque no indica que es el acento principal.

`--color-accent-dark: #6f3fe6`: contiene un morado más oscuro. Se utiliza junto con `--accent` para completar degradados y variaciones del color principal. El número `2` expresa que es una segunda variante, pero no su función exacta.

`--color-border-subtle: rgba(255,255,255,.12)`: contiene blanco con una opacidad del 12 %. Se utiliza para crear bordes y líneas muy sutiles sobre superficies oscuras. El nombre es corto y comprensible dentro del CSS, aunque no indica expresamente que representa un borde translúcido.

Las variables estructurales de Film Rails y las variables visuales de Claqueta viven en sus respectivos módulos y se documentan en `docs/css/layout.md`.

Los antiguos tokens de valor `#0b0712` y `#14ffe9` se eliminaron porque no tenían consumidores ni literales equivalentes con una responsabilidad reutilizable. El valor `#120a1f` sí forma parte de una superficie reutilizable y quedó representado por `--color-surface-base`.
