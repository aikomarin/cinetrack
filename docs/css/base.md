## css/base/reset.css

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
  color: var(--color-text-primary);
  font-family: var(--font-family-body);
  background: linear-gradient(180deg, #0b0516 0%, #2a0f4f 100%) fixed;
}
```

`color: var(--color-text-primary)`: aplica el color general del texto de la aplicación. Actualmente `--color-text-primary` contiene `#f6f3ff`, un blanco muy claro con un matiz violeta que contrasta con los fondos oscuros.

`font-family: var(--font-family-body)`: aplica la tipografía general de lectura. Actualmente `--font-family-body` contiene `'DM Sans', system-ui, sans-serif`; utiliza DM Sans cuando está disponible y recurre a la fuente del sistema o a una fuente sans serif si no puede cargarla.

`background: linear-gradient(180deg, #0b0516 0%, #2a0f4f 100%) fixed`: crea un degradado vertical que comienza con un violeta casi negro (`#0b0516`) en la parte superior y termina con un morado oscuro (`#2a0f4f`) en la parte inferior. `fixed` mantiene el fondo inmóvil mientras el contenido se desplaza.

---

```css
header.cinedock-wrapper,
.page-rails,
main {
  z-index: auto;
}
```

`z-index: auto`: deja que el encabezado, el contenedor de los rails y el contenido principal utilicen el orden normal de apilamiento, sin imponer un nivel numérico propio.
