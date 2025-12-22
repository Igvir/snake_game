# 🟢 Prompt: Menú de Pausa

## Objetivo
Agregar funcionalidad de pausa al juego.

## Contexto Actual
- Juego corre continuamente
- Solo se puede salir con ESC

## Tarea
Implementar pausa que:
1. Se active con ESPACIO
2. Muestre mensaje "PAUSED"
3. Congele el juego hasta reanudar

## Archivos a Modificar
- `snake_game.py`: Bucle principal y manejo de eventos

## Código Base Necesario

```python
# Variable de estado:
paused = False

# En el manejo de eventos:
elif event.key == pygame.K_SPACE:
    paused = not paused

# En el bucle principal:
if not paused:
    # Lógica del juego existente
else:
    # Mostrar mensaje de pausa
    pause_text = font.render("PAUSED - Press SPACE to continue", True, WHITE)
    screen.blit(pause_text, (WINDOW_SIZE//2 - 150, WINDOW_SIZE//2))
```

## Criterios de Éxito
- [ ] ESPACIO pausa/reanuda el juego
- [ ] Mensaje visible durante pausa
- [ ] Serpiente no se mueve en pausa
- [ ] Controles siguen funcionando

## Pruebas
```bash
python snake_game.py
# Presiona ESPACIO durante el juego
```

## Tiempo Estimado
15-20 minutos
