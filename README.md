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

## Estructura del Curso
Una guia completa del curso puede encontrarse en los archivos [Curso Python](./curso_python_primaria.md) y [Guía GIT](./guia_git_curso.md). El curso está diseñado para 12 semanas (3 meses) y está dividido en 3 bloques principales:

### MES 1: Fundamentos (Semanas 1-4)

* Hola Mundo y conceptos básicos
* Variables y tipos de datos
* Entrada de datos
* Condicionales

### MES 2: Estructuras de Control (Semanas 5-8)

* Ciclos (while y for)
* Listas básicas
* Listas y ciclos combinados
* Proyecto integrador: Mini-Snake en texto

### MES 3: Proyecto Final (Semanas 9-12)

* Funciones
* Introducción a Pygame
* Movimiento y control
* Proyecto final: Juego Snake completo

### Características del Curso

- Progresivo y Adaptado: Cada concepto se construye sobre el anterior
- Práctico: Cada semana tiene actividades prácticas y tareas
- Motivador: Los estudiantes ven progreso constante hacia su juego
- Visual: A partir de la semana 10, trabajan con gráficos reales
- Completo: Incluye código funcional del proyecto final

### Puntos Destacados

- Edad apropiada: Lenguaje y ejemplos adaptados para niños de 11-12 años
- Gamificación: Sistema de puntos y proyectos semanales
- Recursos completos: Incluye material para instructores y estudiantes
- Evaluación clara: 20% participación, 30% tareas, 50% proyecto final
- Extensible: Ideas de mejoras para estudiantes avanzados

El curso culmina con un juego Snake totalmente funcional que incluye todas las características clásicas: movimiento, crecimiento, colisiones, puntuación y sistema de game over/reinicio.


## Instalación del juego
El proyecto incluye un juego completo de ejemplo que uedes instalar siguiendo estas instrucciones. Este código es solo un ejemplo y es ligeramente diferente al que se construye sigueindo el curso.

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
