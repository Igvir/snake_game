# 🐍 Juego Snake en Python

## Descripción

Este es un proyecto educativo diseñado para enseñar conceptos fundamentales de programación en Python a través del desarrollo de un juego clásico: Snake.

## Objetivos de Aprendizaje

- Programación orientada a objetos
- Manejo de eventos y bucles de juego
- Uso de la librería Pygame
- Estructuras de datos (listas)
- Control de flujo y lógica de juego
- Manejo de colisiones

## Requisitos

- Python 3.6 o superior
- Pygame 2.5.2

## Instalación

1. Clona o descarga este repositorio
2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate     # En Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo Jugar

### Opción 1: Ejecutar directamente
```bash
python snake_game.py
```

### Opción 2: Usar el script de ejecución
```bash
./run_game.sh
```

## Controles

- **Flechas del teclado**: Mover la serpiente
- **ESC**: Salir del juego

## Características del Juego

- Serpiente que crece al comer comida
- Sistema de puntuación
- Detección de colisiones con paredes y cuerpo
- Interfaz gráfica simple y clara

## Estructura del Proyecto

```
snake/
├── snake_game.py      # Código principal del juego
├── test_snake.py      # Pruebas unitarias
├── run_game.sh        # Script de ejecución
├── requirements.txt   # Dependencias
└── README.md         # Este archivo
```

## Conceptos de Python Demostrados

- **Clases y objetos**: Estructura del juego
- **Listas**: Manejo del cuerpo de la serpiente
- **Bucles**: Game loop principal
- **Condicionales**: Lógica de colisiones y movimiento
- **Funciones**: Organización del código
- **Módulos**: Importación de librerías

## Pruebas

Ejecuta las pruebas unitarias con:
```bash
python -m pytest test_snake.py
```

## Contribuciones

Este es un proyecto educativo. Las contribuciones son bienvenidas para mejorar la experiencia de aprendizaje.

## Licencia

Proyecto educativo de uso libre.
