## css/base/reset.css

`/* Base: Reinicio del documento */`

Identifica el bloque que establece las reglas generales de reinicio para todo el documento.

---

```css
* {
  box-sizing: border-box;
}
```

`box-sizing: border-box`: hace que el ancho y el alto de todos los elementos incluyan también su `padding` y su `border`, evitando que estos aumenten el tamaño exterior declarado.

---

```css
html,
body {
  height: 100%;
  margin: 0;
}
```

`height: 100%`: hace que `html` y `body` puedan ocupar toda la altura disponible del documento.

`margin: 0`: elimina el margen exterior que el navegador agrega de forma predeterminada alrededor de la página.

## css/base/global.css

```css
body {
  color: var(--ink);
  font-family: var(--text-font);
  background: linear-gradient(180deg, #0b0516 0%, #2a0f4f 100%) fixed;
}
```

`color: var(--ink)`: aplica el color general del texto de la aplicación. Actualmente `--ink` contiene `#f6f3ff`, un blanco muy claro con un matiz violeta que contrasta con los fondos oscuros.

Pendiente de nomenclatura: `--ink` significa “tinta”, pero no indica claramente que representa el color principal del texto. No se modifica todavía porque tiene dependencias en varios archivos.

`font-family: var(--text-font)`: aplica la tipografía general de lectura. Actualmente `--text-font` contiene `'DM Sans', system-ui, sans-serif`; utiliza DM Sans cuando está disponible y recurre a la fuente del sistema o a una fuente sans serif si no puede cargarla.

Pendiente de nomenclatura: `--text-font` indica que es una fuente de texto, pero no especifica claramente que funciona como tipografía general del cuerpo. No se modifica todavía porque tiene dependencias en varios archivos.

`background: linear-gradient(180deg, #0b0516 0%, #2a0f4f 100%) fixed`: crea un degradado vertical que comienza con un violeta casi negro (`#0b0516`) en la parte superior y termina con un morado oscuro (`#2a0f4f`) en la parte inferior. `fixed` mantiene el fondo inmóvil mientras el contenido se desplaza.

---

`/* Layout: Contexto de apilamiento principal */`: identifica el bloque que controla el nivel de apilamiento de la estructura principal de la página.

---

```css
header.cinedock-wrapper,
.page-rails,
main {
  z-index: auto;
}
```

`z-index: auto`: deja que el encabezado, el contenedor de los rails y el contenido principal utilicen el orden normal de apilamiento, sin imponer un nivel numérico propio.
