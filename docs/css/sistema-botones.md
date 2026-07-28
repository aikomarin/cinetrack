# Sistema de botones de CineTrack

## 1. Botón principal

### Uso

Es el botón principal del sistema.

Debe utilizarse para la acción más importante de cada pantalla.

### Aplicaciones

- Agregar.
- Buscar.
- Filtrar.
- Explorar catálogo.
- Ver catálogo.
- Crear.
- Crear maratón.
- Cualquier acción principal equivalente.

### No utilizar para

- Guardar.
- Cancelar.
- Eliminar.
- Acciones pequeñas de tarjetas.
- Navegación contextual.

---

## 2. Botón Guardar

### Uso

Representa cualquier acción que persista información.

Debe utilizarse exclusivamente para operaciones de guardado.

### Aplicaciones

- Guardar.
- Guardar cambios.
- Guardar nombre.
- Guardar desde búsqueda.
- Cualquier acción equivalente.

### No utilizar para

- Buscar.
- Agregar.
- Cancelar.
- Navegación.
- Eliminar.

---

## 3. Botón secundario

### Uso

Representa acciones secundarias o de navegación.

### Aplicaciones

- Volver.
- Cancelar.
- Catálogo.
- App Central.
- Navegación secundaria.
- Cualquier acción equivalente.

### No utilizar para

- Guardar.
- Eliminar.
- Acción principal.

---

## 4. Botón contextual

### Uso

Representa acciones rápidas sobre un elemento específico.

### Aplicaciones

- Editar.
- Ver.
- Limpiar.
- Acciones rápidas equivalentes.

### No utilizar para

- Guardar.
- Cancelar.
- Navegación principal.
- Eliminar.

---

## 5. Botón destructivo

### Uso

Representa acciones que pueden eliminar o quitar información.

Su función es abrir una confirmación antes de ejecutar una acción irreversible.

### Aplicaciones

- Eliminar.
- Quitar.
- Abrir confirmación de eliminación.

### No utilizar para

- Navegación.
- Cancelar.
- Guardar.

---

## 6. Botón de confirmación destructiva

### Uso

Representa la confirmación definitiva de una acción irreversible.

### Aplicaciones

- Sí, eliminar.
- Eliminar saga.
- Eliminar maratón.
- Confirmar eliminación.
- Cualquier acción equivalente.

### No utilizar para

- Navegación.
- Cancelar.
- Guardar.

---

# Componentes excluidos

Los siguientes componentes **no forman parte del sistema global de botones** y deberán documentarse de manera independiente:

- Botón de cierre (`.btn-close`).
- Paginación.
- Navegación de Cinedock.
- Marca de Cinedock.
- Pestañas de Kanban / Focus.
- Activador del selector personalizado.
- Opciones del selector personalizado.

---

# Especificación de implementación

En una segunda fase se definirán las propiedades visuales comunes del sistema de botones, incluyendo:

- Altura.
- Padding.
- Radio.
- Tipografía.
- Iconografía.
- Ancho mínimo.
- Variantes de tamaño.
- Estados:
  - Normal.
  - Hover.
  - Focus.
  - Active.
  - Disabled.

Una vez definidas estas reglas, se procederá a la normalización global del sistema de botones.