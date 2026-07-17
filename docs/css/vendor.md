## Límites con Vendor

Bootstrap 5.3, Bootstrap Icons y el JavaScript `bootstrap.bundle` se cargan desde CDN en `base.html`. Sus clases, atributos y comportamientos pertenecen a Bootstrap y constituyen un contrato externo: no deben renombrarse, trasladarse ni reinterpretarse durante las refactorizaciones de CSS propio. CineTrack puede combinarlos con clases propias o aplicar overrides desde sus módulos, pero no modifica los archivos distribuidos por Bootstrap.

Flatpickr, su hoja de estilos base y la localización española también se cargan desde CDN en `base.html`. Las clases generadas por la librería —por ejemplo `.flatpickr-calendar`, `.flatpickr-day`, `.selected`, `.startRange` y `.endRange`— pertenecen a Flatpickr y no deben renombrarse. Los atributos, estados y estructura que Flatpickr genera se consideran parte de su API de integración.

`css/vendor/flatpickr-theme.css` es código propio de CineTrack situado en la capa Vendor porque adapta visualmente esa integración. El archivo contiene clases propias, como `.ct-date-input` y `.ct-date-input-visible`, junto con overrides que consumen selectores de Flatpickr. Los valores visuales del tema son responsabilidad del proyecto, pero los nombres `.flatpickr-*` y sus estados asociados siguen perteneciendo a la librería y deben conservarse en futuras refactorizaciones. No existen renombres pendientes dentro de esta frontera Vendor.

## css/vendor/flatpickr-theme.css

```css
.ct-date-input,
.ct-date-input-visible {
  min-height: 64px;
  width: 100%;
  padding: 0 18px;

  color: #f7f3ff;
  font-family: "DM Sans", sans-serif;
  font-size: 1rem;
  font-weight: 600;

  background:
    linear-gradient(
      135deg,
      rgba(94, 45, 137, 0.46),
      rgba(40, 52, 112, 0.46)
    );

  border: 1px solid rgba(182, 132, 255, 0.38);
  border-radius: 16px;

  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.06),
    inset 0 -1px 0 rgba(0, 0, 0, 0.18),
    0 0 0 1px rgba(121, 72, 191, 0.08);

  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease,
    background 0.2s ease;
}
```

`min-height: 64px`: establece la altura mínima con el valor `64px`.

`width: 100%`: establece el ancho con el valor `100%`.

`padding: 0 18px`: aplica el espacio interior con el valor `0 18px`.

`color: #f7f3ff`: aplica el color del contenido con el valor `#f7f3ff`.

`font-family: "DM Sans", sans-serif`: aplica la familia tipográfica con el valor `"DM Sans", sans-serif`.

`font-size: 1rem`: establece el tamaño de fuente con el valor `1rem`.

`font-weight: 600`: establece el grosor tipográfico con el valor `600`.

`background: linear-gradient( 135deg, rgba(94, 45, 137, 0.46), rgba(40, 52, 112, 0.46) )`: aplica el fondo con el valor `linear-gradient( 135deg, rgba(94, 45, 137, 0.46), rgba(40, 52, 112, 0.46) )`.

`border: 1px solid rgba(182, 132, 255, 0.38)`: aplica el borde con el valor `1px solid rgba(182, 132, 255, 0.38)`.

`border-radius: 16px`: redondea las esquinas con el valor `16px`.

`box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), inset 0 -1px 0 rgba(0, 0, 0, 0.18), 0 0 0 1px rgba(121, 72, 191, 0.08)`: aplica la sombra con el valor `inset 0 1px 0 rgba(255, 255, 255, 0.06), inset 0 -1px 0 rgba(0, 0, 0, 0.18), 0 0 0 1px rgba(121, 72, 191, 0.08)`.

`transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease`: suaviza los cambios indicados con el valor `border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease`.

---

```css
.ct-date-input-visible:hover {
  border-color: rgba(194, 150, 255, 0.56);

  background:
    linear-gradient(
      135deg,
      rgba(104, 51, 151, 0.52),
      rgba(43, 58, 124, 0.52)
    );
}
```

`border-color: rgba(194, 150, 255, 0.56)`: aplica el color del borde con el valor `rgba(194, 150, 255, 0.56)`.

`background: linear-gradient( 135deg, rgba(104, 51, 151, 0.52), rgba(43, 58, 124, 0.52) )`: aplica el fondo con el valor `linear-gradient( 135deg, rgba(104, 51, 151, 0.52), rgba(43, 58, 124, 0.52) )`.

---

```css
.ct-date-input-visible:focus {
  color: #ffffff;

  background:
    linear-gradient(
      135deg,
      rgba(112, 55, 166, 0.58),
      rgba(47, 64, 137, 0.58)
    );

  border-color: rgba(166, 101, 255, 0.95);

  box-shadow:
    0 0 0 3px rgba(143, 76, 255, 0.16),
    0 0 22px rgba(129, 66, 230, 0.28),
    inset 0 1px 0 rgba(255, 255, 255, 0.08);

  outline: none;
}
```

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

`background: linear-gradient( 135deg, rgba(112, 55, 166, 0.58), rgba(47, 64, 137, 0.58) )`: aplica el fondo con el valor `linear-gradient( 135deg, rgba(112, 55, 166, 0.58), rgba(47, 64, 137, 0.58) )`.

`border-color: rgba(166, 101, 255, 0.95)`: aplica el color del borde con el valor `rgba(166, 101, 255, 0.95)`.

`box-shadow: 0 0 0 3px rgba(143, 76, 255, 0.16), 0 0 22px rgba(129, 66, 230, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.08)`: aplica la sombra con el valor `0 0 0 3px rgba(143, 76, 255, 0.16), 0 0 22px rgba(129, 66, 230, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.08)`.

`outline: none`: aplica el contorno con el valor `none`.

---

```css
.ct-date-input-visible::placeholder {
  color: rgba(239, 230, 255, 0.6);
  font-weight: 500;
}
```

`color: rgba(239, 230, 255, 0.6)`: aplica el color del contenido con el valor `rgba(239, 230, 255, 0.6)`.

`font-weight: 500`: establece el grosor tipográfico con el valor `500`.

---

```css
.flatpickr-calendar {
  width: 330px;

  padding: 8px;

  color: #f4edff;

  background:
    radial-gradient(
      circle at top right,
      rgba(119, 63, 203, 0.22),
      transparent 42%
    ),
    linear-gradient(
      160deg,
      #1a0d2c 0%,
      #12091f 58%,
      #0e0819 100%
    );

  border: 1px solid rgba(183, 125, 255, 0.42);
  border-radius: 20px;

  box-shadow:
    0 22px 60px rgba(0, 0, 0, 0.56),
    0 0 34px rgba(119, 59, 210, 0.24),
    inset 0 1px 0 rgba(255, 255, 255, 0.05);

  overflow: hidden;
}
```

`width: 330px`: establece el ancho con el valor `330px`.

`padding: 8px`: aplica el espacio interior con el valor `8px`.

`color: #f4edff`: aplica el color del contenido con el valor `#f4edff`.

`background: radial-gradient( circle at top right, rgba(119, 63, 203, 0.22), transparent 42% ), linear-gradient( 160deg, #1a0d2c 0%, #12091f 58%, #0e0819 100% )`: aplica el fondo con el valor `radial-gradient( circle at top right, rgba(119, 63, 203, 0.22), transparent 42% ), linear-gradient( 160deg, #1a0d2c 0%, #12091f 58%, #0e0819 100% )`.

`border: 1px solid rgba(183, 125, 255, 0.42)`: aplica el borde con el valor `1px solid rgba(183, 125, 255, 0.42)`.

`border-radius: 20px`: redondea las esquinas con el valor `20px`.

`box-shadow: 0 22px 60px rgba(0, 0, 0, 0.56), 0 0 34px rgba(119, 59, 210, 0.24), inset 0 1px 0 rgba(255, 255, 255, 0.05)`: aplica la sombra con el valor `0 22px 60px rgba(0, 0, 0, 0.56), 0 0 34px rgba(119, 59, 210, 0.24), inset 0 1px 0 rgba(255, 255, 255, 0.05)`.

`overflow: hidden`: controla el contenido desbordado con el valor `hidden`.

---

```css
.flatpickr-months {
  min-height: 52px;

  background:
    linear-gradient(
      135deg,
      rgba(112, 55, 170, 0.92),
      rgba(51, 54, 126, 0.92)
    );

  border-radius: 14px 14px 10px 10px;
}
```

`min-height: 52px`: establece la altura mínima con el valor `52px`.

`background: linear-gradient( 135deg, rgba(112, 55, 170, 0.92), rgba(51, 54, 126, 0.92) )`: aplica el fondo con el valor `linear-gradient( 135deg, rgba(112, 55, 170, 0.92), rgba(51, 54, 126, 0.92) )`.

`border-radius: 14px 14px 10px 10px`: redondea las esquinas con el valor `14px 14px 10px 10px`.

---

```css
.flatpickr-month {
  color: #ffffff;
}
```

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

---

```css
.flatpickr-current-month {
  padding-top: 11px;

  color: #ffffff;
  font-family: "Teko", sans-serif;
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: 0.035em;
}
```

`padding-top: 11px`: aplica el espacio interior superior con el valor `11px`.

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

`font-family: "Teko", sans-serif`: aplica la familia tipográfica con el valor `"Teko", sans-serif`.

`font-size: 1.25rem`: establece el tamaño de fuente con el valor `1.25rem`.

`font-weight: 600`: establece el grosor tipográfico con el valor `600`.

`letter-spacing: 0.035em`: separa las letras con el valor `0.035em`.

---

```css
.flatpickr-current-month .flatpickr-monthDropdown-months,
.flatpickr-current-month input.cur-year {
  color: #ffffff;
  font-family: "Teko", sans-serif;
  font-size: 1.18rem;
  font-weight: 600;

  background: transparent;
  border: 0;
}
```

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

`font-family: "Teko", sans-serif`: aplica la familia tipográfica con el valor `"Teko", sans-serif`.

`font-size: 1.18rem`: establece el tamaño de fuente con el valor `1.18rem`.

`font-weight: 600`: establece el grosor tipográfico con el valor `600`.

`background: transparent`: aplica el fondo con el valor `transparent`.

`border: 0`: aplica el borde con el valor `0`.

---

```css
.flatpickr-current-month .flatpickr-monthDropdown-months:hover,
.flatpickr-current-month input.cur-year:hover {
  background: rgba(255, 255, 255, 0.08);
}
```

`background: rgba(255, 255, 255, 0.08)`: aplica el fondo con el valor `rgba(255, 255, 255, 0.08)`.

---

```css
.flatpickr-monthDropdown-month {
  color: #f6efff;
  background: #1a0d2c;
}
```

`color: #f6efff`: aplica el color del contenido con el valor `#f6efff`.

`background: #1a0d2c`: aplica el fondo con el valor `#1a0d2c`.

---

```css
.flatpickr-prev-month,
.flatpickr-next-month {
  top: 8px;

  width: 38px;
  height: 38px;

  color: #f4edff !important;
  fill: #f4edff !important;

  border-radius: 12px;

  transition:
    background 0.2s ease,
    transform 0.2s ease,
    box-shadow 0.2s ease;
}
```

`top: 8px`: sitúa el borde superior con el valor `8px`.

`width: 38px`: establece el ancho con el valor `38px`.

`height: 38px`: establece la altura con el valor `38px`.

`color: #f4edff !important`: aplica el color del contenido con el valor `#f4edff !important`.

`fill: #f4edff !important`: aplica el relleno SVG con el valor `#f4edff !important`.

`border-radius: 12px`: redondea las esquinas con el valor `12px`.

`transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease`: suaviza los cambios indicados con el valor `background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease`.

---

```css
.flatpickr-prev-month:hover,
.flatpickr-next-month:hover {
  background: rgba(255, 255, 255, 0.11);
  box-shadow: 0 0 14px rgba(181, 125, 255, 0.24);
  transform: scale(1.04);
}
```

`background: rgba(255, 255, 255, 0.11)`: aplica el fondo con el valor `rgba(255, 255, 255, 0.11)`.

`box-shadow: 0 0 14px rgba(181, 125, 255, 0.24)`: aplica la sombra con el valor `0 0 14px rgba(181, 125, 255, 0.24)`.

`transform: scale(1.04)`: aplica la transformación con el valor `scale(1.04)`.

---

```css
.flatpickr-prev-month svg,
.flatpickr-next-month svg {
  fill: currentColor;
}
```

`fill: currentColor`: aplica el relleno SVG con el valor `currentColor`.

---

```css
.flatpickr-weekdays {
  margin-top: 8px;
  padding: 4px 0 6px;

  background: transparent;
}
```

`margin-top: 8px`: aplica el margen superior con el valor `8px`.

`padding: 4px 0 6px`: aplica el espacio interior con el valor `4px 0 6px`.

`background: transparent`: aplica el fondo con el valor `transparent`.

---

```css
span.flatpickr-weekday {
  color: rgba(230, 216, 249, 0.74);

  font-family: "DM Sans", sans-serif;
  font-size: 0.76rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.045em;
}
```

`color: rgba(230, 216, 249, 0.74)`: aplica el color del contenido con el valor `rgba(230, 216, 249, 0.74)`.

`font-family: "DM Sans", sans-serif`: aplica la familia tipográfica con el valor `"DM Sans", sans-serif`.

`font-size: 0.76rem`: establece el tamaño de fuente con el valor `0.76rem`.

`font-weight: 700`: establece el grosor tipográfico con el valor `700`.

`text-transform: uppercase`: transforma visualmente el texto con el valor `uppercase`.

`letter-spacing: 0.045em`: separa las letras con el valor `0.045em`.

---

```css
.flatpickr-days,
.dayContainer {
  width: 100%;
  min-width: 100%;
  max-width: 100%;
}
```

`width: 100%`: establece el ancho con el valor `100%`.

`min-width: 100%`: establece el ancho mínimo con el valor `100%`.

`max-width: 100%`: establece el ancho máximo con el valor `100%`.

---

```css
.flatpickr-day {
  width: 38px;
  max-width: 38px;
  height: 38px;
  line-height: 38px;

  margin: 2px;

  color: #e9def8;

  font-family: "DM Sans", sans-serif;
  font-size: 0.92rem;
  font-weight: 600;

  border: 1px solid transparent;
  border-radius: 12px;

  transition:
    color 0.15s ease,
    background 0.15s ease,
    border-color 0.15s ease,
    transform 0.15s ease,
    box-shadow 0.15s ease;
}
```

`width: 38px`: establece el ancho con el valor `38px`.

`max-width: 38px`: establece el ancho máximo con el valor `38px`.

`height: 38px`: establece la altura con el valor `38px`.

`line-height: 38px`: establece la altura de línea con el valor `38px`.

`margin: 2px`: aplica el margen exterior con el valor `2px`.

`color: #e9def8`: aplica el color del contenido con el valor `#e9def8`.

`font-family: "DM Sans", sans-serif`: aplica la familia tipográfica con el valor `"DM Sans", sans-serif`.

`font-size: 0.92rem`: establece el tamaño de fuente con el valor `0.92rem`.

`font-weight: 600`: establece el grosor tipográfico con el valor `600`.

`border: 1px solid transparent`: aplica el borde con el valor `1px solid transparent`.

`border-radius: 12px`: redondea las esquinas con el valor `12px`.

`transition: color 0.15s ease, background 0.15s ease, border-color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease`: suaviza los cambios indicados con el valor `color 0.15s ease, background 0.15s ease, border-color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease`.

---

```css
.flatpickr-day:hover,
.flatpickr-day:focus {
  color: #ffffff;

  background:
    linear-gradient(
      135deg,
      rgba(149, 82, 255, 0.32),
      rgba(85, 72, 206, 0.32)
    );

  border-color: rgba(177, 123, 255, 0.32);

  box-shadow:
    0 0 14px rgba(138, 74, 238, 0.2);

  transform: translateY(-1px);
}
```

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

`background: linear-gradient( 135deg, rgba(149, 82, 255, 0.32), rgba(85, 72, 206, 0.32) )`: aplica el fondo con el valor `linear-gradient( 135deg, rgba(149, 82, 255, 0.32), rgba(85, 72, 206, 0.32) )`.

`border-color: rgba(177, 123, 255, 0.32)`: aplica el color del borde con el valor `rgba(177, 123, 255, 0.32)`.

`box-shadow: 0 0 14px rgba(138, 74, 238, 0.2)`: aplica la sombra con el valor `0 0 14px rgba(138, 74, 238, 0.2)`.

`transform: translateY(-1px)`: aplica la transformación con el valor `translateY(-1px)`.

---

```css
.flatpickr-day.today {
  color: #ffffff;

  border-color: rgba(179, 121, 255, 0.85);

  box-shadow:
    inset 0 0 0 1px rgba(179, 121, 255, 0.18),
    0 0 12px rgba(143, 81, 239, 0.2);
}
```

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

`border-color: rgba(179, 121, 255, 0.85)`: aplica el color del borde con el valor `rgba(179, 121, 255, 0.85)`.

`box-shadow: inset 0 0 0 1px rgba(179, 121, 255, 0.18), 0 0 12px rgba(143, 81, 239, 0.2)`: aplica la sombra con el valor `inset 0 0 0 1px rgba(179, 121, 255, 0.18), 0 0 12px rgba(143, 81, 239, 0.2)`.

---

```css
.flatpickr-day.today:hover {
  background: rgba(150, 84, 255, 0.26);
}
```

`background: rgba(150, 84, 255, 0.26)`: aplica el fondo con el valor `rgba(150, 84, 255, 0.26)`.

---

```css
.flatpickr-day.selected,
.flatpickr-day.startRange,
.flatpickr-day.endRange {
  color: #ffffff;

  background:
    linear-gradient(
      135deg,
      #ad68ff 0%,
      #8646f6 48%,
      #5e4ee3 100%
    );

  border-color: transparent;

  box-shadow:
    0 0 0 2px rgba(176, 111, 255, 0.16),
    0 0 20px rgba(139, 75, 241, 0.48);

  transform: scale(1.03);
}
```

`color: #ffffff`: aplica el color del contenido con el valor `#ffffff`.

`background: linear-gradient( 135deg, #ad68ff 0%, #8646f6 48%, #5e4ee3 100% )`: aplica el fondo con el valor `linear-gradient( 135deg, #ad68ff 0%, #8646f6 48%, #5e4ee3 100% )`.

`border-color: transparent`: aplica el color del borde con el valor `transparent`.

`box-shadow: 0 0 0 2px rgba(176, 111, 255, 0.16), 0 0 20px rgba(139, 75, 241, 0.48)`: aplica la sombra con el valor `0 0 0 2px rgba(176, 111, 255, 0.16), 0 0 20px rgba(139, 75, 241, 0.48)`.

`transform: scale(1.03)`: aplica la transformación con el valor `scale(1.03)`.

---

```css
.flatpickr-day.prevMonthDay,
.flatpickr-day.nextMonthDay,
.flatpickr-day.flatpickr-disabled {
  color: rgba(221, 205, 241, 0.28);
}
```

`color: rgba(221, 205, 241, 0.28)`: aplica el color del contenido con el valor `rgba(221, 205, 241, 0.28)`.

---

```css
.flatpickr-day.flatpickr-disabled:hover {
  background: transparent;
  border-color: transparent;
  box-shadow: none;
  transform: none;
}
```

`background: transparent`: aplica el fondo con el valor `transparent`.

`border-color: transparent`: aplica el color del borde con el valor `transparent`.

`box-shadow: none`: aplica la sombra con el valor `none`.

`transform: none`: aplica la transformación con el valor `none`.

---

```css
.flatpickr-calendar.arrowTop::before {
  border-bottom-color: rgba(183, 125, 255, 0.42);
}
```

`border-bottom-color: rgba(183, 125, 255, 0.42)`: aplica el color del borde inferior con el valor `rgba(183, 125, 255, 0.42)`.

---

```css
.flatpickr-calendar.arrowTop::after {
  border-bottom-color: #1a0d2c;
}
```

`border-bottom-color: #1a0d2c`: aplica el color del borde inferior con el valor `#1a0d2c`.

---

```css
.flatpickr-calendar.arrowBottom::before {
  border-top-color: rgba(183, 125, 255, 0.42);
}
```

`border-top-color: rgba(183, 125, 255, 0.42)`: aplica el color del borde superior con el valor `rgba(183, 125, 255, 0.42)`.

---

```css
.flatpickr-calendar.arrowBottom::after {
  border-top-color: #12091f;
}
```

`border-top-color: #12091f`: aplica el color del borde superior con el valor `#12091f`.
