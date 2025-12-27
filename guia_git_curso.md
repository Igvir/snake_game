# 🌳 Guía de Git para el Curso de Python
## Control de Versiones para Niños

---

## 🤔 ¿Qué es Git?

Git es como una **máquina del tiempo para tu código**. Te permite:
- Guardar diferentes versiones de tu programa
- Volver atrás si algo se rompe
- Ver todo lo que has hecho
- Trabajar en diferentes ideas al mismo tiempo (usando ramas)

**Analogía para niños:**
Imagina que estás escribiendo una historia. Git es como tener copias de cada capítulo que escribes, para que si borras algo por accidente, puedas recuperarlo.

---

## 🚀 Instalación de Git

### Windows:
1. Ve a https://git-scm.com
2. Descarga "Git for Windows"
3. Instala con todas las opciones por defecto
4. Abre "Git Bash" desde el menú inicio

### Mac:
1. Abre Terminal
2. Escribe: `git --version`
3. Si no está instalado, te pedirá instalarlo
4. O descarga desde https://git-scm.com

### Linux:
```bash
sudo apt install git  # Ubuntu/Debian
sudo yum install git  # Fedora
```

### Verificar instalación:
```bash
git --version
# Deberías ver algo como: git version 2.40.0
```

---

## ⚙️ Configuración Inicial (Solo una vez)

```bash
# Tu nombre (usa tu nombre real)
git config --global user.name "María García"

# Tu email
git config --global user.email "maria@example.com"

# Verificar configuración
git config --list
```

**¡Importante!** Esta configuración solo se hace UNA VEZ en tu computadora.

---

## 📝 Comandos Básicos de Git

### 1. Iniciar un Proyecto

```bash
# Crear carpeta para tu proyecto
mkdir mi-juego-snake
cd mi-juego-snake

# Iniciar Git en esta carpeta
git init

# Verificar que funcionó
git status
```

**Explicación:**
- `mkdir`: Make Directory (crear carpeta)
- `cd`: Change Directory (entrar a la carpeta)
- `git init`: Iniciar repositorio Git
- `git status`: Ver qué está pasando

---

### 2. Ver el Estado de tu Proyecto

```bash
git status
```

**¿Qué verás?**
- Archivos nuevos (en rojo)
- Archivos modificados (en rojo)
- Archivos listos para guardar (en verde)

---

### 3. Agregar Archivos

```bash
# Agregar un archivo específico
git add hola_mundo.py

# Agregar todos los archivos
git add .

# Ver qué agregaste
git status
```

**Analogía:** Es como poner cosas en una caja antes de cerrarla.

---

### 4. Guardar Cambios (Commit)

```bash
# Guardar con un mensaje
git commit -m "Mi primer programa"

# Ver qué guardaste
git log --oneline
```

**Mensajes de commit buenos:**
- ✅ "Agregué función para mover serpiente"
- ✅ "Corregí error en detección de colisiones"
- ❌ "cambios" (muy vago)
- ❌ "asd" (no dice nada)

---

### 5. Ver el Historial

```bash
# Historial simple
git log --oneline

# Historial con gráfico
git log --graph --all --oneline

# Últimos 5 commits
git log -5 --oneline
```

---

## 🌿 Trabajar con Ramas

### ¿Qué es una Rama?

Una rama es como una **línea de tiempo alternativa** donde puedes experimentar sin afectar tu código principal.

```
main:       A---B---C---D
                 \
semana-01:        E---F
```

### Crear y Usar Ramas

```bash
# Ver ramas existentes
git branch

# Crear nueva rama
git branch semana-01

# Cambiar a esa rama
git checkout semana-01

# Crear Y cambiar a nueva rama (atajo)
git checkout -b semana-01
```

### Volver a la Rama Principal

```bash
git checkout main
```

### Fusionar Ramas (Merge)

```bash
# Primero, ve a main
git checkout main

# Luego, fusiona tu rama
git merge semana-01
```

**Analogía:** Es como copiar tu tarea del cuaderno de borrador al cuaderno limpio.

---

## 🏷️ Tags (Etiquetas)

Los tags son como **marcadores de libros** para versiones importantes.

```bash
# Crear un tag
git tag mes-1-completo

# Ver todos los tags
git tag -l

# Tag con descripción
git tag -a v1.0 -m "Versión final del juego"

# Ver info de un tag
git show mes-1-completo
```

---

## 📊 Flujo de Trabajo Semanal

### Cada Semana Seguirás Este Proceso:

```bash
# 1. Ir a la rama principal
git checkout main

# 2. Crear rama de la semana
git checkout -b semana-XX

# 3. Escribir tu código
# ... programa en Python ...

# 4. Ver qué cambió
git status

# 5. Agregar archivos
git add .

# 6. Guardar cambios
git commit -m "Semana XX: descripción de lo que hiciste"

# 7. Volver a main
git checkout main

# 8. Fusionar tu trabajo
git merge semana-XX

# 9. Ver tu progreso
git log --oneline
```

---

## 🎯 Ejemplo Completo de la Semana 1

```bash
# Paso 1: Configurar (solo primera vez)
cd ~/Documentos
mkdir curso-python
cd curso-python
git init

# Paso 2: Crear README
echo "# Mi Curso de Python" > README.md
git add README.md
git commit -m "Inicio del proyecto"

# Paso 3: Crear rama semana 1
git checkout -b semana-01

# Paso 4: Crear programa
# Aquí escribes tu código en hola_mundo.py

# Paso 5: Guardar
git add hola_mundo.py
git commit -m "Semana 1: Primer programa con print"

# Paso 6: Ver qué hiciste
git log --oneline

# Paso 7: Fusionar a main
git checkout main
git merge semana-01

# Paso 8: Celebrar 🎉
git log --graph --all --oneline
```

---

## 🆘 Comandos de Ayuda

```bash
# Ver ayuda general
git help

# Ayuda de un comando específico
git help add
git help commit

# Versión corta de ayuda
git add -h
```

---

## ⚠️ Errores Comunes y Soluciones

### Error 1: "No git repository found"
**Solución:** No has hecho `git init` en esta carpeta.
```bash
git init
```

### Error 2: "Nothing to commit"
**Solución:** No has agregado archivos con `git add`.
```bash
git add .
git commit -m "tu mensaje"
```

### Error 3: "Please tell me who you are"
**Solución:** No has configurado tu nombre.
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Error 4: Olvidé en qué rama estoy
**Solución:**
```bash
git branch
# La rama con * es donde estás
```

### Error 5: Quiero deshacer el último commit
**Solución (¡cuidado!):**
```bash
# Mantener los cambios
git reset --soft HEAD~1

# O pregunta al profesor
```

---

## 🎮 Ejercicios Prácticos de Git

### Ejercicio 1: Mi Primer Repositorio
```bash
# 1. Crea una carpeta llamada "practica-git"
# 2. Entra a la carpeta
# 3. Inicializa Git
# 4. Crea un archivo llamado "yo.txt" con tu nombre
# 5. Haz un commit
# 6. Ve el historial
```

### Ejercicio 2: Trabajando con Ramas
```bash
# 1. Crea una rama llamada "experimento"
# 2. Cambia a esa rama
# 3. Crea un archivo "prueba.py"
# 4. Haz commit
# 5. Vuelve a main
# 6. Fusiona "experimento" con main
```

### Ejercicio 3: Historia del Proyecto
```bash
# 1. Haz 3 commits diferentes
# 2. Crea un tag llamado "version-1"
# 3. Haz 2 commits más
# 4. Ve todo el historial con gráfico
```

---

## 📈 Progreso del Curso con Git

### Estructura de Ramas del Proyecto Snake:

```
main (rama principal)
  |
  |-- semana-01 (Hola Mundo)
  |     |
  |     └─> merge to main
  |
  |-- semana-02 (Variables)
  |     |
  |     └─> merge to main
  |
  |-- semana-03 (Input)
  |     |
  |     └─> merge to main
  |
  ... (continúa hasta semana-12)
  |
  |-- semana-12-final (Snake Completo)
        |
        └─> merge to main --> TAG: v1.0
```

### Tags Importantes del Curso:

- `mes-1-completo`: Finalización del primer mes
- `mes-2-completo`: Finalización del segundo mes (Mini-Snake texto)
- `v1.0-snake-completo`: Juego final terminado

---

## 🎨 Visualizando tu Progreso

### Ver Todo el Proyecto de Forma Visual:

```bash
# Gráfico completo del proyecto
git log --all --graph --decorate --oneline

# Ver archivos en cada commit
git log --name-status --oneline

# Estadísticas del proyecto
git shortlog -s -n
```

### Comparar Versiones:

```bash
# Ver diferencias entre ramas
git diff semana-01 semana-02

# Ver qué cambió en un archivo
git diff hola_mundo.py

# Ver cambios desde hace 3 commits
git diff HEAD~3
```

---

## 🏆 Buenas Prácticas

### ✅ DO (Hacer):
1. **Hacer commits frecuentemente** (cada vez que algo funciona)
2. **Escribir mensajes claros** ("Agregué sistema de puntuación")
3. **Usar ramas para cada semana**
4. **Fusionar cuando el código funcione**
5. **Ver el log regularmente** para ver tu progreso

### ❌ DON'T (No hacer):
1. **No hacer commits de código que no funciona** (prueba antes)
2. **No usar mensajes vagos** ("cambios", "update")
3. **No trabajar sin hacer commits** (podrías perder trabajo)
4. **No tener miedo de Git** (¡siempre puedes pedir ayuda!)

---

## 📚 Comandos de Referencia Rápida

### Inicio y Configuración:
```bash
git init                              # Iniciar repositorio
git config --global user.name "..."  # Configurar nombre
git config --global user.email "..." # Configurar email
```

### Trabajo Diario:
```bash
git status                    # Ver estado
git add archivo.py            # Agregar archivo
git add .                     # Agregar todo
git commit -m "mensaje"       # Guardar cambios
git log --oneline             # Ver historial
```

### Ramas:
```bash
git branch                    # Ver ramas
git branch nombre-rama        # Crear rama
git checkout nombre-rama      # Cambiar a rama
git checkout -b nombre-rama   # Crear y cambiar
git merge nombre-rama         # Fusionar rama
```

### Tags:
```bash
git tag nombre-tag            # Crear tag
git tag -l                    # Ver tags
git tag -a v1.0 -m "msg"     # Tag con mensaje
```

### Información:
```bash
git log --graph --all        # Historial visual
git diff                     # Ver cambios
git show commit-id           # Ver commit específico
```

---

## 🎓 Objetivos de Aprendizaje Git

### Al finalizar el curso, deberías poder:

- ✅ Inicializar un repositorio Git
- ✅ Hacer commits de tu código
- ✅ Crear y cambiar entre ramas
- ✅ Fusionar ramas
- ✅ Crear tags para versiones importantes
- ✅ Ver el historial de tu proyecto
- ✅ Entender por qué Git es útil
- ✅ Usar Git en futuros proyectos

---

## 🎮 Proyecto Final: Tu Portafolio en Git

Al terminar el curso, tu repositorio mostrará:

```
mi-juego-snake/
├── README.md               # Descripción del proyecto
├── requirements.txt        # Dependencias (pygame)
├── hola_mundo.py          # Semana 1
├── variables.py           # Semana 2
├── entrada_datos.py       # Semana 3
├── condicionales.py       # Semana 4
├── ciclos.py              # Semana 5
├── listas.py              # Semana 6
├── listas_avanzadas.py    # Semana 7
├── mini_snake.py          # Semana 8
├── funciones.py           # Semana 9
├── ventana_basica.py      # Semana 10
├── movimiento.py          # Semana 11
└── snake_game.py          # Semana 12 (FINAL)
```

Con un historial completo de 12 semanas mostrando tu evolución como programador.

---

## 💡 Para Padres y Tutores

### ¿Por qué enseñamos Git a niños?

1. **Organización:** Aprenden a mantener su trabajo ordenado
2. **Responsabilidad:** Cada cambio tiene un autor y fecha
3. **Recuperación:** No pierden trabajo si algo sale mal
4. **Profesionalismo:** Herramienta usada por programadores reales
5. **Portafolio:** Demostrable en el futuro

### ¿Es muy complicado para ellos?

No, si se enseña progresivamente. Usamos solo 10-12 comandos básicos durante todo el curso, introducidos gradualmente.

### ¿Necesitan cuenta de GitHub?

No es necesario para el curso básico. Git funciona completamente en su computadora. GitHub es opcional para compartir proyectos.

---

## 🌟 Recursos Adicionales

### Sitios Web:
- **Git oficial:** https://git-scm.com
- **Try Git:** https://try.github.io (tutorial interactivo)
- **GitHub:** https://github.com (opcional, para compartir)

### Videos Recomendados (en español):
- "Git y GitHub para principiantes" en YouTube
- Tutoriales de código facilito
- Cursos de Platzi (Git desde cero)

### Libros:
- "Pro Git" (gratis en git-scm.com/book)
- Capítulos básicos son suficientes para el curso

---

## 🎉 ¡Mensaje Final sobre Git!

Git puede parecer complicado al principio, pero recuerda:

- **No tengas miedo de experimentar** - Es difícil romper algo permanentemente
- **Haz commits frecuentemente** - Es mejor tener muchos que pocos
- **Pide ayuda si te atoras** - Todos los programadores hemos estado ahí
- **Celebra tu progreso** - Cada commit es un logro

Git es como andar en bicicleta: al principio necesitas ayuda, pero una vez que lo aprendes, nunca lo olvidas.

**¡Ahora tienes superpoderes de control de versiones!** 🦸‍♂️🦸‍♀️

---

## 📞 Comandos de Emergencia

Si algo sale mal, usa estos comandos (con supervisión del profesor):

```bash
# Ver en qué rama estás
git branch

# Descartar cambios NO guardados en un archivo
git checkout -- archivo.py

# Ver el estado actual
git status

# Volver al último commit (CUIDADO)
git reset --hard HEAD

# Si estás perdido, pide ayuda al profesor
# ¡No borres la carpeta .git!
```

---

**Versión:** 1.0 - Curso Python 6to Grado
**Última actualización:** 2025