# 🔴 Prompt: Arquitectura Orientada a Objetos

## Objetivo
Refactorizar el código a una estructura más orientada a objetos.

## Contexto Actual
- Código principalmente procedural en `main()`
- Clase Snake básica
- Lógica mezclada

## Tarea
Crear estructura OOP con:
1. Clase `Game` que maneje el estado
2. Clase `Food` para la comida
3. Clase `UI` para la interfaz
4. Separar responsabilidades

## Archivos a Crear/Modificar
- `snake_game.py`: Refactorizar completamente
- `game_objects.py`: Nuevas clases

## Estructura Propuesta

```python
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.ui = UI()
        self.score = 0
        self.running = True
    
    def run(self):
        # Bucle principal
    
    def update(self):
        # Lógica de actualización
    
    def render(self, screen):
        # Renderizado

class Food:
    def __init__(self):
        self.position = self.generate_position()
    
    def generate_position(self):
        # Generar posición aleatoria

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
    
    def draw_score(self, screen, score):
        # Dibujar puntuación
```

## Criterios de Éxito
- [ ] Código organizado en clases
- [ ] Responsabilidades separadas
- [ ] Funcionalidad mantenida
- [ ] Código más mantenible

## Pruebas
```bash
python -m pytest test_snake.py
python snake_game.py
```

## Tiempo Estimado
2-3 horas
