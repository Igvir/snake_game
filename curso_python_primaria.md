# 🐍 Curso de Python para 6to Grado
## Aprende a Programar Creando tu Propio Juego Snake

### 📋 Información General del Curso

**Duración:** 12 semanas (3 meses)
**Edad:** 11-12 años (6to grado de primaria)
**Nivel:** Principiante - Sin experiencia previa requerida
**Objetivo Final:** Crear tu propio juego Snake funcional usando Python y Git

### 🌳 Estructura Git del Proyecto

El curso utiliza Git y ramas para seguir la evolución del proyecto:
- **main:** Rama principal con el proyecto final
- **semana-01:** Primera versión (Hola Mundo)
- **semana-02:** Agrega variables
- **semana-03:** Agrega entrada de datos
- Y así sucesivamente hasta **semana-12**

Cada estudiante tendrá su propio repositorio local y aprenderá a:
- Guardar versiones de su código
- Ver el historial de cambios
- Recuperar versiones anteriores si algo sale mal
- Trabajar de manera organizada

---

## 🎯 Objetivos del Curso

Al finalizar este curso, los estudiantes podrán:
- Entender los conceptos básicos de programación
- Escribir código en Python
- Crear variables y usar diferentes tipos de datos
- Usar ciclos y condicionales
- Crear funciones básicas
- Desarrollar un videojuego sencillo
- **Usar Git para controlar versiones de su código**
- **Trabajar con ramas para organizar el desarrollo**
- **Entender el flujo de trabajo de un proyecto de software**

---

## 📚 Estructura del Curso

### **SEMANA 0: Preparación del Entorno (Sesión Inicial)**

**Objetivo:** Configurar todas las herramientas necesarias

#### Instalación y Configuración:

**1. Instalar Python**
- Descargar desde python.org
- Verificar instalación: `python --version`

**2. Instalar Git**
- Descargar desde git-scm.com
- Verificar instalación: `git --version`

**3. Configurar Git por Primera Vez**
```bash
# Configurar nombre (usar tu nombre real)
git config --global user.name "María García"

# Configurar email
git config --global user.email "maria@example.com"

# Verificar configuración
git config --list
```

**4. Crear el Proyecto**
```bash
# Crear carpeta del proyecto
mkdir mi-juego-snake
cd mi-juego-snake

# Inicializar Git
git init

# Crear primer archivo
echo "# Mi Juego Snake" > README.md

# Ver estado
git status

# Agregar archivo
git add README.md

# Hacer primer commit
git commit -m "Inicio del proyecto Snake"
```

**Conceptos Git de la Semana 0:**
- **Repositorio:** Carpeta donde Git guarda el historial
- **Commit:** Fotografía de tu código en un momento específico
- **git init:** Crear un nuevo repositorio
- **git status:** Ver qué cambios hay
- **git add:** Preparar archivos para guardar
- **git commit:** Guardar los cambios

**Actividad Práctica:**
Cada estudiante crea su propio repositorio y hace su primer commit con un archivo README.md que contenga:
- Su nombre
- El nombre de su juego
- La fecha de inicio

---

### **MES 1: Fundamentos de Python**

#### **Semana 1: ¡Hola Mundo! - Primeros Pasos en Python**

**Conceptos:**
- ¿Qué es programar?
- ¿Qué es Python?
- El primer programa: "Hola Mundo"
- La función `print()`
- Comentarios en código

**Actividades Prácticas:**
```python
# Mi primer programa
print("¡Hola! Soy un programador")
print("Voy a crear un juego")

# Ejercicio 1: Presenta tu juego
print("Mi juego se llamará: Snake")
print("El jugador controlará una serpiente")
```

**Proyecto de la Semana:**
Crear un programa que imprima 5 mensajes sobre el juego que van a crear.

**Git de la Semana 1:**
```bash
# Crear rama para la semana 1
git checkout -b semana-01

# Crear archivo del programa
# (escribir el código en hola_mundo.py)

# Ver cambios
git status

# Agregar archivo nuevo
git add hola_mundo.py

# Guardar cambios con mensaje descriptivo
git commit -m "Semana 1: Primer programa con print"

# Ver historial
git log --oneline

# Volver a main y fusionar
git checkout main
git merge semana-01
```

**Conceptos Git de la Semana:**
- **Rama (branch):** Línea de desarrollo independiente
- **git checkout -b:** Crear y cambiar a una nueva rama
- **git merge:** Unir cambios de una rama a otra
- **git log:** Ver historial de commits

**Tarea:**
- Escribir un programa que imprima tu nombre, edad y color favorito
- Agregar al menos 3 comentarios explicando qué hace cada línea
- Hacer commit de tu trabajo con un mensaje claro
- **Git:** Asegurarte de estar en la rama semana-01

---

#### **Semana 2: Variables y Tipos de Datos**

**Conceptos:**
- ¿Qué son las variables?
- Números enteros (int)
- Números decimales (float)
- Texto (strings)
- Operaciones matemáticas básicas

**Actividades Prácticas:**
```python
# Variables del juego
nombre_jugador = "María"
puntuacion = 0
velocidad_serpiente = 5.0
juego_activo = True

print("Jugador:", nombre_jugador)
print("Puntuación inicial:", puntuacion)

# Aumentamos la puntuación
puntuacion = puntuacion + 10
print("Nueva puntuación:", puntuacion)
```

**Proyecto de la Semana:**
Crear un programa que simule el marcador de un juego usando variables.

**Git de la Semana 2:**
```bash
# Crear nueva rama desde main
git checkout main
git checkout -b semana-02

# Crear archivo con variables
# (escribir código en variables.py)

# Guardar cambios
git add variables.py
git commit -m "Semana 2: Variables y tipos de datos"

# Si modificaste archivos de la semana anterior
git add hola_mundo.py
git commit -m "Semana 2: Mejorado programa de la semana 1"

# Fusionar a main
git checkout main
git merge semana-02

# Ver todas las ramas
git branch
```

**Conceptos Git de la Semana:**
- **git branch:** Ver todas las ramas
- **Commits múltiples:** Puedes hacer varios commits en una rama
- **Mensajes descriptivos:** Importancia de describir bien los cambios

**Tarea:**
- Crear variables para: nombre del jugador, nivel, vidas y puntos
- Hacer operaciones que cambien estos valores
- Imprimir los resultados
- **Git:** Trabajar en rama semana-02 y hacer al menos 2 commits

---

#### **Semana 3: Entrada de Datos y Conversiones**

**Conceptos:**
- La función `input()`
- Conversión de tipos de datos
- Concatenación de strings
- Interpolación de strings (f-strings)

**Actividades Prácticas:**
```python
# Pidiendo datos al jugador
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")

print(f"¡Hola {nombre}! Tienes {edad} años")

# Para el juego
nivel = input("¿Qué nivel quieres jugar? (1-5): ")
nivel_numero = int(nivel)

if nivel_numero > 3:
    print("¡Nivel difícil seleccionado!")
else:
    print("Nivel fácil seleccionado")
```

**Proyecto de la Semana:**
Crear un programa que pida el nombre del jugador y configure opciones del juego.

**Git de la Semana 3:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-03

# Trabajar en entrada_datos.py
git add entrada_datos.py
git commit -m "Semana 3: Input y conversiones de tipos"

# Ver diferencias con semana anterior
git diff semana-02

# Fusionar a main
git checkout main
git merge semana-03
```

**Conceptos Git de la Semana:**
- **git diff:** Ver diferencias entre ramas o commits
- **Evolución del proyecto:** Cómo el código crece cada semana

**Tarea:**
- Crear un programa que pida: nombre, edad y comida favorita
- Usar estos datos para crear un mensaje personalizado
- Pedir un número y multiplicarlo por 5
- **Git:** Hacer commit cuando el programa funcione correctamente

---

#### **Semana 4: Condicionales - Tomando Decisiones**

**Conceptos:**
- Operadores de comparación (==, !=, >, <, >=, <=)
- Estructura if, elif, else
- Operadores lógicos (and, or, not)
- Booleanos (True/False)

**Actividades Prácticas:**
```python
# Simulando colisiones en el juego
posicion_serpiente = 250
posicion_comida = 300
posicion_muro = 500

if posicion_serpiente == posicion_comida:
    print("¡Comida capturada! +10 puntos")
elif posicion_serpiente >= posicion_muro:
    print("¡Chocaste con el muro! Game Over")
else:
    print("Sigue jugando...")

# Sistema de vidas
vidas = 3

if vidas > 0:
    print("Todavía puedes jugar")
else:
    print("Game Over - Sin vidas")
```

**Proyecto de la Semana:**
Crear un mini-juego de texto donde el jugador toma decisiones y recibe diferentes resultados.

**Git de la Semana 4:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-04

# Trabajar en condicionales.py
git add condicionales.py
git commit -m "Semana 4: If, elif y else implementados"

# Ver todo el historial del proyecto
git log --graph --all --oneline

# Fusionar
git checkout main
git merge semana-04

# Crear un tag para marcar fin del mes 1
git tag mes-1-completo
git tag -l
```

**Conceptos Git de la Semana:**
- **git tag:** Marcar versiones importantes
- **git log --graph:** Ver el historial visualmente
- **Hitos del proyecto:** Celebrar el primer mes completado

**Tarea:**
- Crear un programa que determine si ganaste o perdiste según puntos
- Usar al menos 3 condiciones diferentes (if, elif, else)
- Incluir operadores lógicos (and/or)
- **Git:** Crear un tag "mes-1-completo" después de fusionar

---

### **MES 2: Estructuras de Control y Listas**

#### **Semana 5: Ciclos - El Poder de la Repetición**

**Conceptos:**
- Ciclo `while`
- Ciclo `for`
- `break` y `continue`
- Contadores

**Actividades Prácticas:**
```python
# Simulando el movimiento de la serpiente
movimientos = 0

while movimientos < 5:
    print(f"La serpiente se mueve... paso {movimientos + 1}")
    movimientos = movimientos + 1

print("¡Serpiente detenida!")

# Contando puntos
for puntos in range(0, 51, 10):
    print(f"Puntuación: {puntos}")

# Game loop simple
jugando = True
turnos = 0

while jugando and turnos < 10:
    print(f"Turno {turnos + 1}")
    accion = input("¿Seguir jugando? (s/n): ")
    if accion == "n":
        jugando = False
    turnos = turnos + 1
```

**Proyecto de la Semana:**
Crear un juego simple de adivinanza de números usando un ciclo while.

**Git de la Semana 5:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-05

# Trabajar en ciclos.py
git add ciclos.py
git commit -m "Semana 5: Ciclos while y for"

# Ver cambios desde la semana 4
git diff semana-04 semana-05

# Fusionar
git checkout main
git merge semana-05
```

**Conceptos Git de la Semana:**
- **Comparar ramas:** Ver diferencias entre semanas
- **Seguimiento de progreso:** Cada rama muestra una etapa del aprendizaje

**Tarea:**
- Crear un programa que cuente del 1 al 20 con un ciclo for
- Crear un programa que repita acciones hasta que el usuario diga "salir"
- Crear un contador regresivo desde 10 hasta 0
- **Git:** Hacer un commit por cada programa completado

---

#### **Semana 6: Listas - Organizando Información**

**Conceptos:**
- ¿Qué son las listas?
- Crear listas
- Acceder a elementos (índices)
- Agregar y eliminar elementos
- Longitud de listas

**Actividades Prácticas:**
```python
# La serpiente como una lista
cuerpo_serpiente = [1, 2, 3]
print("Cuerpo inicial:", cuerpo_serpiente)

# La serpiente crece
cuerpo_serpiente.append(4)
print("Serpiente creció:", cuerpo_serpiente)

# Posiciones de la serpiente
posiciones_x = [100, 120, 140]
posiciones_y = [200, 200, 200]

print("Cabeza en:", posiciones_x[0], posiciones_y[0])
print("Cola en:", posiciones_x[-1], posiciones_y[-1])

# Puntuaciones altas
puntuaciones_altas = [100, 85, 70, 55, 40]
print("Mejor puntuación:", puntuaciones_altas[0])
print("Total de puntuaciones:", len(puntuaciones_altas))
```

**Proyecto de la Semana:**
Crear un programa que maneje una lista de jugadores y sus puntuaciones.

**Git de la Semana 6:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-06

# Trabajar en listas.py
git add listas.py
git commit -m "Semana 6: Listas y operaciones básicas"

# Fusionar
git checkout main
git merge semana-06
```

**Tarea:**
- Crear una lista con 5 nombres de amigos
- Agregar 2 nombres más
- Eliminar un nombre
- Imprimir cada nombre usando un ciclo for
- **Git:** Asegurarte de que tu código esté guardado en la rama semana-06

---

#### **Semana 7: Listas y Ciclos Juntos**

**Conceptos:**
- Recorrer listas con for
- Modificar elementos de listas
- Listas dentro de listas (básico)
- Buscar elementos en listas

**Actividades Prácticas:**
```python
# Moviendo cada parte del cuerpo de la serpiente
cuerpo_serpiente = [1, 2, 3, 4, 5]

print("Posiciones originales:")
for posicion in cuerpo_serpiente:
    print(f"Segmento en: {posicion}")

# Mover toda la serpiente
for i in range(len(cuerpo_serpiente)):
    cuerpo_serpiente[i] = cuerpo_serpiente[i] + 1

print("Después de moverse:")
for posicion in cuerpo_serpiente:
    print(f"Segmento en: {posicion}")

# Buscar comida
posiciones_comida = [50, 100, 150, 200]
posicion_serpiente = 100

if posicion_serpiente in posiciones_comida:
    print("¡Comida encontrada!")
else:
    print("Sigue buscando...")
```

**Proyecto de la Semana:**
Simular el movimiento de la serpiente usando listas de coordenadas.

**Git de la Semana 7:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-07

# Trabajar en listas_avanzadas.py
git add listas_avanzadas.py
git commit -m "Semana 7: Listas y ciclos combinados"

# Fusionar
git checkout main
git merge semana-07
```

**Tarea:**
- Crear una lista de 10 números
- Usar un ciclo para sumar 5 a cada número
- Crear una lista de palabras y imprimirlas una por una
- Contar cuántos números son mayores a 50 en una lista
- **Git:** Trabajar en rama semana-07

---

#### **Semana 8: Proyecto Integrador del Mes 2**

**Proyecto: Mini-Snake en Texto**

Crear una versión simplificada del juego Snake en modo texto que incluya:
- Una serpiente representada como lista
- Comida en posiciones aleatorias
- Sistema de puntuación
- Detección de colisiones básica
- Game loop

**Git de la Semana 8:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-08

# Trabajar en mini_snake.py
git add mini_snake.py
git commit -m "Semana 8: Mini-Snake versión texto completo"

# Fusionar
git checkout main
git merge semana-08

# Crear tag para el segundo mes
git tag mes-2-completo

# Guardar todo en un archivo de respaldo
git log --all --oneline > historial.txt
git add historial.txt
git commit -m "Historial del mes 2"
```

**Conceptos Git de la Semana:**
- **Proyecto completo:** Primer juego funcional guardado en Git
- **Tags importantes:** Marcar versiones jugables
- **Documentación:** Guardar el historial del proyecto

**Ejemplo del Proyecto:**
```python
import random

# Configuración inicial
serpiente = [5, 4, 3]
comida = random.randint(1, 10)
puntos = 0
jugando = True

print("=== MINI SNAKE ===")
print("La serpiente está en:", serpiente)

while jugando:
    print(f"\nPuntos: {puntos}")
    print(f"Serpiente: {serpiente}")
    print(f"Comida en: {comida}")
    
    # Mover serpiente
    direccion = input("¿Hacia dónde? (derecha/izquierda/salir): ")
    
    if direccion == "salir":
        jugando = False
        continue
    
    # Mover cabeza
    cabeza = serpiente[0]
    if direccion == "derecha":
        cabeza = cabeza + 1
    elif direccion == "izquierda":
        cabeza = cabeza - 1
    
    # Verificar colisión con comida
    if cabeza == comida:
        print("¡Comida capturada!")
        puntos = puntos + 10
        serpiente.insert(0, cabeza)
        comida = random.randint(1, 10)
    else:
        # Mover serpiente
        serpiente.insert(0, cabeza)
        serpiente.pop()
    
    # Verificar colisión con bordes
    if cabeza < 0 or cabeza > 10:
        print("¡Chocaste con el borde!")
        jugando = False

print(f"\n=== GAME OVER ===")
print(f"Puntuación final: {puntos}")
```

---

### **MES 3: Funciones y Proyecto Final**

#### **Semana 9: Funciones - Organizando el Código**

**Conceptos:**
- ¿Qué son las funciones?
- Definir funciones con `def`
- Parámetros y argumentos
- Valor de retorno con `return`
- Funciones sin return

**Actividades Prácticas:**
```python
# Función simple para saludar
def saludar_jugador(nombre):
    print(f"¡Bienvenido al juego, {nombre}!")

saludar_jugador("Carlos")

# Función para calcular puntos
def calcular_puntos(comidas_capturadas):
    puntos = comidas_capturadas * 10
    return puntos

mi_puntuacion = calcular_puntos(5)
print(f"Puntos totales: {mi_puntuacion}")

# Función para verificar colisión
def hay_colision(posicion_serpiente, posicion_objeto):
    if posicion_serpiente == posicion_objeto:
        return True
    else:
        return False

if hay_colision(100, 100):
    print("¡Colisión detectada!")

# Función para mover serpiente
def mover_serpiente(serpiente, direccion):
    cabeza = serpiente[0]
    if direccion == "arriba":
        cabeza = cabeza - 1
    elif direccion == "abajo":
        cabeza = cabeza + 1
    serpiente.insert(0, cabeza)
    serpiente.pop()
    return serpiente
```

**Proyecto de la Semana:**
Reorganizar el Mini-Snake de la semana 8 usando funciones.

**Git de la Semana 9:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-09

# Mejorar mini_snake.py con funciones
git add mini_snake.py
git commit -m "Semana 9: Refactorización con funciones"

# Crear funciones.py con ejemplos
git add funciones.py
git commit -m "Semana 9: Ejemplos de funciones"

# Fusionar
git checkout main
git merge semana-09
```

**Tarea:**
- Crear 3 funciones diferentes para el juego
- Una función que reciba un nombre y devuelva un saludo
- Una función que calcule el área de un rectángulo
- Una función que determine si un número es par o impar
- **Git:** Hacer commits separados para cada función nueva

---

#### **Semana 10: Introducción a Pygame**

**Conceptos:**
- ¿Qué es Pygame?
- Instalación de Pygame
- Crear una ventana
- Colores en RGB
- El game loop básico
- Cerrar la ventana correctamente

**Actividades Prácticas:**
```python
import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 600
ALTO = 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Primer Juego")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Game loop
jugando = True
while jugando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    
    # Dibujar
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, VERDE, (100, 100, 50, 50))
    
    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
```

**Proyecto de la Semana:**
Crear una ventana con diferentes formas (círculos, cuadrados) de colores.

**Git de la Semana 10:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-10

# Crear archivo requirements.txt
echo "pygame==2.5.2" > requirements.txt
git add requirements.txt
git commit -m "Semana 10: Dependencias de Pygame"

# Crear primer programa con Pygame
git add ventana_basica.py
git commit -m "Semana 10: Primera ventana con Pygame"

# Fusionar
git checkout main
git merge semana-10
```

**Conceptos Git de la Semana:**
- **requirements.txt:** Documentar dependencias del proyecto
- **Cambio importante:** Transición de texto a gráficos

**Tarea:**
- Crear una ventana de 800x600 píxeles
- Cambiar el color de fondo
- Dibujar al menos 3 formas diferentes
- Agregar un título personalizado a la ventana
- **Git:** Commit cuando el programa muestre la ventana correctamente

---

#### **Semana 11: Movimiento y Control del Jugador**

**Conceptos:**
- Detectar teclas presionadas
- Mover objetos en la pantalla
- Variables de posición (x, y)
- Coordenadas en Pygame
- Control de velocidad (FPS)

**Actividades Prácticas:**
```python
import pygame

pygame.init()

# Configuración
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Posición inicial de la "serpiente"
x = 300
y = 200
velocidad = 5

jugando = True
while jugando:
    reloj.tick(30)  # 30 FPS
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    
    # Control de movimiento
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    
    # Dibujar
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, VERDE, (x, y, 20, 20))
    pygame.display.flip()

pygame.quit()
```

**Proyecto de la Semana:**
Crear un cuadrado que se mueva por la pantalla y no salga de los bordes.

**Git de la Semana 11:**
```bash
# Nueva rama
git checkout main
git checkout -b semana-11

# Crear programa con movimiento
git add movimiento.py
git commit -m "Semana 11: Control de movimiento implementado"

# Agregar límites de pantalla
git add movimiento.py
git commit -m "Semana 11: Límites de pantalla añadidos"

# Fusionar
git checkout main
git merge semana-11
```

**Tarea:**
- Agregar límites para que el objeto no salga de la ventana
- Cambiar la velocidad del movimiento
- Agregar un segundo objeto controlado con W, A, S, D
- **Git:** Hacer un commit después de cada funcionalidad nueva

---

#### **Semana 12: Proyecto Final - Juego Snake Completo**

**Proyecto Final: Desarrollar el Juego Snake**

Integrar todos los conceptos aprendidos para crear el juego completo.

**Git de la Semana 12:**
```bash
# Nueva rama para el proyecto final
git checkout main
git checkout -b semana-12-final

# Crear el archivo principal del juego
git add snake_game.py
git commit -m "Semana 12: Estructura base del Snake"

# Agregar funcionalidades paso a paso
git add snake_game.py
git commit -m "Semana 12: Movimiento de serpiente"

git add snake_game.py
git commit -m "Semana 12: Sistema de comida"

git add snake_game.py
git commit -m "Semana 12: Detección de colisiones"

git add snake_game.py
git commit -m "Semana 12: Sistema de puntuación"

git add snake_game.py
git commit -m "Semana 12: Game Over y reinicio"

# Actualizar README con instrucciones
git add README.md
git commit -m "Semana 12: Documentación completa"

# Fusionar a main
git checkout main
git merge semana-12-final

# Crear tag de versión final
git tag v1.0-snake-completo
git tag -a v1.0 -m "Versión 1.0: Juego Snake completado"

# Ver todo el proyecto
git log --graph --all --oneline --decorate
```

**Conceptos Git de la Semana:**
- **Commits incrementales:** Guardar cada funcionalidad
- **Versión final:** Tag para marcar el proyecto completo
- **Documentación:** README actualizado con instrucciones
- **Historial completo:** Ver toda la evolución del proyecto

**Flujo de Trabajo Completo:**
```bash
# Ver todas las ramas creadas
git branch -a

# Ver todos los tags
git tag -l

# Ver estadísticas del proyecto
git log --oneline --graph --all

# Crear un archivo con el historial completo
git log --all --pretty=format:"%h %ad | %s%d [%an]" --date=short > proyecto_completo.txt
```

**Características del Juego:**
1. Serpiente que se mueve con las flechas
2. Comida que aparece en posiciones aleatorias
3. La serpiente crece al comer
4. Sistema de puntuación
5. Detección de colisión con paredes
6. Detección de colisión con el propio cuerpo
7. Game Over y reinicio

**Estructura del Código:**
```python
import pygame
import random

# Inicialización
pygame.init()

# Constantes
ANCHO = 600
ALTO = 400
TAMANO_CELDA = 20
VELOCIDAD_JUEGO = 10

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Funciones del juego
def dibujar_serpiente(ventana, cuerpo_serpiente):
    """Dibuja cada segmento de la serpiente"""
    for segmento in cuerpo_serpiente:
        pygame.draw.rect(ventana, VERDE, 
                        (segmento[0], segmento[1], 
                         TAMANO_CELDA, TAMANO_CELDA))

def generar_comida():
    """Genera posición aleatoria para la comida"""
    x = random.randrange(0, ANCHO, TAMANO_CELDA)
    y = random.randrange(0, ALTO, TAMANO_CELDA)
    return [x, y]

def verificar_colision(cabeza, cuerpo):
    """Verifica si la cabeza choca con el cuerpo"""
    return cabeza in cuerpo[1:]

def verificar_bordes(x, y):
    """Verifica si la serpiente choca con los bordes"""
    return x < 0 or x >= ANCHO or y < 0 or y >= ALTO

# Configuración inicial
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")
reloj = pygame.time.Clock()

# Variables del juego
def iniciar_juego():
    x, y = ANCHO // 2, ALTO // 2
    cuerpo_serpiente = [[x, y]]
    direccion = "DERECHA"
    cambio_direccion = direccion
    comida = generar_comida()
    puntos = 0
    return x, y, cuerpo_serpiente, direccion, cambio_direccion, comida, puntos

x, y, cuerpo_serpiente, direccion, cambio_direccion, comida, puntos = iniciar_juego()

# Game loop principal
jugando = True
game_over = False

while jugando:
    while game_over:
        ventana.fill(NEGRO)
        fuente = pygame.font.Font(None, 50)
        texto = fuente.render(f"Game Over! Puntos: {puntos}", True, ROJO)
        ventana.blit(texto, (ANCHO//4, ALTO//3))
        
        fuente_pequena = pygame.font.Font(None, 30)
        texto2 = fuente_pequena.render("Presiona C para jugar o Q para salir", True, BLANCO)
        ventana.blit(texto2, (ANCHO//6, ALTO//2))
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
                game_over = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    jugando = False
                    game_over = False
                if evento.key == pygame.K_c:
                    game_over = False
                    x, y, cuerpo_serpiente, direccion, cambio_direccion, comida, puntos = iniciar_juego()
    
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion != "ABAJO":
                cambio_direccion = "ARRIBA"
            elif evento.key == pygame.K_DOWN and direccion != "ARRIBA":
                cambio_direccion = "ABAJO"
            elif evento.key == pygame.K_LEFT and direccion != "DERECHA":
                cambio_direccion = "IZQUIERDA"
            elif evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                cambio_direccion = "DERECHA"
    
    # Actualizar dirección
    direccion = cambio_direccion
    
    # Mover serpiente
    if direccion == "ARRIBA":
        y -= TAMANO_CELDA
    elif direccion == "ABAJO":
        y += TAMANO_CELDA
    elif direccion == "IZQUIERDA":
        x -= TAMANO_CELDA
    elif direccion == "DERECHA":
        x += TAMANO_CELDA
    
    # Actualizar cuerpo
    cabeza = [x, y]
    cuerpo_serpiente.insert(0, cabeza)
    
    # Verificar si comió
    if x == comida[0] and y == comida[1]:
        puntos += 10
        comida = generar_comida()
    else:
        cuerpo_serpiente.pop()
    
    # Verificar colisiones
    if verificar_bordes(x, y) or verificar_colision(cabeza, cuerpo_serpiente):
        game_over = True
    
    # Dibujar
    ventana.fill(NEGRO)
    dibujar_serpiente(ventana, cuerpo_serpiente)
    pygame.draw.rect(ventana, ROJO, (comida[0], comida[1], TAMANO_CELDA, TAMANO_CELDA))
    
    # Mostrar puntuación
    fuente = pygame.font.Font(None, 35)
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    ventana.blit(texto_puntos, (10, 10))
    
    pygame.display.flip()
    reloj.tick(VELOCIDAD_JUEGO)

pygame.quit()
```

**Actividades de la Semana 12:**
1. Implementar el código completo
2. Probar el juego y corregir errores
3. Agregar mejoras personales:
   - Cambiar colores
   - Ajustar velocidad
   - Agregar niveles de dificultad
   - Agregar sonidos (opcional)

---

## 🎓 Evaluación y Reconocimiento

### Criterios de Evaluación:
- **Participación en clase:** 20%
- **Tareas semanales:** 30%
- **Proyecto final:** 50%

### Certificado de Finalización:
Los estudiantes que completen el curso recibirán un certificado que incluye:
- Nombre del estudiante
- Fecha de finalización
- Conceptos dominados
- Captura de pantalla de su juego

---

## 🎮 Recursos Adicionales

### Para el Instructor:
- Preparar una computadora con Python y Pygame instalados
- Tener ejemplos visuales para cada concepto
- Crear un entorno de práctica seguro
- Mantener copias de respaldo del código

### Para los Estudiantes:
- Instalar Python 3.8 o superior
- **Instalar Git desde git-scm.com**
- Instalar Pygame: `pip install pygame`
- Tener un editor de código (IDLE, VS Code, o Thonny)
- Carpeta para guardar todos los proyectos
- **Cuenta de GitHub (opcional, para compartir proyectos)**

### Comandos Git Esenciales (Referencia Rápida):
```bash
# Configuración inicial
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Comandos básicos
git init                    # Iniciar repositorio
git status                  # Ver estado
git add archivo.py          # Agregar archivo
git commit -m "mensaje"     # Guardar cambios
git log --oneline           # Ver historial

# Trabajo con ramas
git branch                  # Ver ramas
git checkout -b semana-X    # Crear y cambiar a rama
git checkout main           # Volver a main
git merge semana-X          # Fusionar rama

# Tags
git tag nombre-tag          # Crear tag
git tag -l                  # Ver tags
```

### Páginas Web Recomendadas:
- Python.org (documentación oficial)
- Pygame.org (documentación de Pygame)
- Code.org (ejercicios adicionales)

---

## 💡 Consejos Pedagógicos

### Para Mantener el Interés:
1. **Gamificar el aprendizaje:** Sistema de puntos por tareas completadas
2. **Proyectos visibles:** Que vean resultados inmediatos
3. **Trabajo en parejas:** Programación por pares ocasionalmente
4. **Desafíos opcionales:** Para estudiantes más avanzados
5. **Celebrar errores:** Los errores son oportunidades de aprendizaje

### Manejo de Dificultades:
- **Estudiantes adelantados:** Agregar características extra al juego
- **Estudiantes con dificultades:** Más tiempo de práctica y ejemplos simplificados
- **Errores comunes:** Mantener una lista de soluciones a errores frecuentes

### Sesiones de Clase Sugeridas:
- **15 min:** Repaso de la semana anterior
- **25 min:** Explicación de nuevos conceptos
- **15 min:** Práctica guiada
- **20 min:** Trabajo independiente
- **10 min:** Presentación de trabajos y cierre

---

## 🏆 Proyecto de Extensión (Opcional)

Para estudiantes que terminen antes o quieran más desafíos:

### Ideas de Mejoras al Juego:
1. **Sistema de niveles:** Aumentar velocidad con puntos
2. **Obstáculos:** Agregar paredes en el mapa
3. **Power-ups:** Comida especial que da bonus
4. **Modo 2 jugadores:** Dos serpientes compitiendo
5. **Tabla de puntuaciones:** Guardar mejores puntajes
6. **Efectos de sonido:** Agregar música y sonidos
7. **Menú principal:** Pantalla de inicio profesional
8. **Diferentes modos:** Clásico, sin bordes, con tiempo límite

---

## 📝 Material de Apoyo

### Glosario de Términos:

**Programación:**
- **Variable:** Contenedor para guardar información
- **Función:** Bloque de código reutilizable
- **Ciclo:** Repetición de instrucciones
- **Condicional:** Decisión en el código
- **Lista:** Colección ordenada de elementos
- **Bug:** Error en el código
- **Debug:** Proceso de encontrar y corregir errores
- **Game loop:** Ciclo principal de un juego
- **FPS:** Cuadros por segundo

**Git:**
- **Repositorio:** Carpeta donde Git guarda todo el historial
- **Commit:** Fotografía del código en un momento específico
- **Rama (Branch):** Línea de desarrollo independiente
- **Main:** Rama principal del proyecto
- **Merge:** Unir cambios de una rama a otra
- **Tag:** Etiqueta para marcar versiones importantes
- **Status:** Estado actual de los archivos
- **Log:** Historial de todos los commits
- **Add:** Preparar archivos para hacer commit
- **Push:** Enviar cambios a GitHub (opcional)
- **Pull:** Traer cambios desde GitHub (opcional)

### Atajos de Teclado Útiles:
- **Ctrl + C:** Copiar
- **Ctrl + V:** Pegar
- **Ctrl + Z:** Deshacer
- **Ctrl + S:** Guardar
- **F5:** Ejecutar programa (en IDLE)

---

## ✅ Lista de Verificación para Instructores

### Antes del Curso:
- [ ] Python instalado en todas las computadoras
- [ ] **Git instalado en todas las computadoras**
- [ ] Pygame instalado y probado
- [ ] Material de cada semana preparado
- [ ] Ejemplos de código funcionando
- [ ] Carpeta compartida para recursos
- [ ] **Repositorio de ejemplo configurado**
- [ ] **Guía rápida de comandos Git impresa**

### Durante el Curso:
- [ ] Asistencia de estudiantes
- [ ] Seguimiento de progreso individual
- [ ] **Verificar que estudiantes hagan commits semanales**
- [ ] Resolución de dudas
- [ ] Revisión de tareas
- [ ] Motivación y reconocimiento
- [ ] **Ayudar con conflictos de Git (si ocurren)**

### Después del Curso:
- [ ] Evaluación final de estudiantes
- [ ] Encuesta de satisfacción
- [ ] Entrega de certificados
- [ ] Documentación de mejoras para futuras ediciones
- [ ] **Compilar enlaces a repositorios de estudiantes (opcional)**

---

## 🎉 ¡Mensaje Final!

Este curso está diseñado para ser divertido, educativo y empoderador. Los estudiantes no solo aprenderán a programar, sino que crearán algo tangible que pueden mostrar con orgullo a sus amigos y familia.

**Recuerda:** El objetivo no es solo aprender Python, sino despertar la pasión por la programación y el pensamiento computacional.

¡Que comience la aventura de programar! 🚀🐍