# 🟢 Bug: Colisión en Esquinas

## Problema
La serpiente ocasionalmente atraviesa las paredes en las esquinas.

## Síntomas
- Serpiente aparece del otro lado de la pantalla
- Ocurre principalmente en esquinas
- Inconsistente, no siempre pasa

## Investigación Sugerida

### 1. Revisar Método de Colisión
```python
# En Snake.check_collision() - línea ~32
def check_collision(self):
    head = self.body[0]
    return (head[0] < 0 or head[0] >= CELLS or 
            head[1] < 0 or head[1] >= CELLS or 
            head in self.body[1:])
```

### 2. Verificar Constantes
```python
# Verificar que CELLS sea correcto
print(f"WINDOW_SIZE: {WINDOW_SIZE}")
print(f"CELL_SIZE: {CELL_SIZE}")  
print(f"CELLS: {CELLS}")
```

### 3. Debug de Posición
```python
# Agregar en move():
print(f"Head position: {new_head}, Limits: 0 to {CELLS-1}")
```

## Posibles Causas
- Cálculo incorrecto de límites
- Condición de colisión mal implementada
- Timing en el bucle de juego

## Solución Esperada
Colisión detectada correctamente en todos los bordes.

## Pruebas
```bash
# Prueba manual
python snake_game.py
# Dirigir serpiente a cada esquina

# Prueba automatizada
python -m pytest test_snake.py::test_collision -v
```

## Tiempo Estimado
30-60 minutos
