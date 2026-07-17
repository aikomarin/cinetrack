## css/utilities/text.css

```css
.detail-text {
  font-size: .975rem;
  line-height: 1.55;
  color: var(--color-text-primary, #e9e9e9);
  opacity: .92;
}
```

`.detail-text` define la tipografía descriptiva compartida por Detail y Search. Conserva el tamaño, la altura de línea, el color con fallback y la opacidad que producía la cascada antes de su consolidación.

---

```css
.detail-text-justified {
  text-align: justify;
}
```

`text-align: justify`: distribuye el espacio entre las palabras para que el texto quede alineado tanto en el borde izquierdo como en el derecho.
