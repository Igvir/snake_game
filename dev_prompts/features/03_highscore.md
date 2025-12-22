# 🟡 Prompt: High Score System

## Objetivo
Implementar sistema de puntuación máxima persistente.

## Contexto Actual
- Puntuación actual se pierde al cerrar
- No hay registro de mejores puntuaciones

## Tarea
Agregar sistema que:
1. Guarde high score en archivo
2. Muestre record actual en pantalla
3. Celebre nuevos records

## Archivos a Modificar
- `snake_game.py`: Funciones de carga/guardado
- `highscore.txt`: Archivo de datos (nuevo)

## Código Base Necesario

```python
import json

def load_highscore():
    try:
        with open('highscore.txt', 'r') as f:
            return int(f.read().strip())
    except:
        return 0

def save_highscore(score):
    with open('highscore.txt', 'w') as f:
        f.write(str(score))

# En main():
highscore = load_highscore()

# Al terminar el juego:
if score > highscore:
    save_highscore(score)
    # Mostrar mensaje de nuevo record
```

## Criterios de Éxito
- [ ] High score se guarda entre sesiones
- [ ] Record se muestra en pantalla
- [ ] Mensaje especial para nuevo record

## Tiempo Estimado
25-30 minutos
