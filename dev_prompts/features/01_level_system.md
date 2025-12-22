# 🟡 Prompt: Sistema de Niveles

## Objetivo
Implementar un sistema de niveles que aumente la dificultad progresivamente.

## Contexto Actual
- Juego básico funcional en `snake_game.py`
- Puntuación simple implementada
- Velocidad fija del juego

## Tarea
Agregar sistema de niveles que:
1. Incremente velocidad cada 50 puntos
2. Muestre nivel actual en pantalla
3. Cambie color de serpiente por nivel

## Archivos a Modificar
- `snake_game.py`: Función main() y clase Snake

## Código Base Necesario

```python
# Variables a agregar en main():
level = 1
base_speed = 10
speed_increment = 2

# Lógica de nivel (después de comer comida):
if score % 50 == 0 and score > 0:
    level = score // 50 + 1
    current_speed = base_speed + (level - 1) * speed_increment

# Colores por nivel:
level_colors = [
    (0, 255, 0),    # Verde - Nivel 1
    (0, 0, 255),    # Azul - Nivel 2  
    (255, 255, 0),  # Amarillo - Nivel 3
    (255, 0, 255),  # Magenta - Nivel 4+
]
```

## Criterios de Éxito
- [ ] Velocidad aumenta cada 50 puntos
- [ ] Nivel se muestra en pantalla
- [ ] Color de serpiente cambia
- [ ] Juego sigue funcionando correctamente

## Pruebas
```bash
python snake_game.py
# Juega hasta conseguir 50+ puntos y verifica cambios
```

## Tiempo Estimado
30-45 minutos
