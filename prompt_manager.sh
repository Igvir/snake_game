#!/bin/bash

# Script para gestionar prompts de desarrollo
# Uso: ./prompt_manager.sh [comando] [opciones]

PROMPTS_DIR="dev_prompts"

show_help() {
    echo "🐍 Snake Game - Gestor de Prompts de Desarrollo"
    echo ""
    echo "Uso: $0 [comando] [opciones]"
    echo ""
    echo "Comandos:"
    echo "  list [categoria]     - Listar prompts disponibles"
    echo "  show <archivo>       - Mostrar contenido de un prompt"
    echo "  create <nombre>      - Crear nuevo prompt desde plantilla"
    echo "  help                 - Mostrar esta ayuda"
    echo ""
    echo "Categorías:"
    echo "  features  - Nuevas funcionalidades"
    echo "  bugs      - Solución de problemas"
    echo "  refactor  - Mejoras de código"
    echo ""
    echo "Ejemplos:"
    echo "  $0 list features"
    echo "  $0 show features/01_level_system.md"
    echo "  $0 create features/mi_nueva_feature"
}

list_prompts() {
    local category=${1:-""}
    
    if [ -z "$category" ]; then
        echo "📋 Todos los prompts disponibles:"
        find $PROMPTS_DIR -name "*.md" -not -path "*/templates/*" | sort
    else
        echo "📋 Prompts en categoría '$category':"
        find $PROMPTS_DIR/$category -name "*.md" 2>/dev/null | sort
    fi
}

show_prompt() {
    local file="$1"
    
    if [ -z "$file" ]; then
        echo "❌ Error: Especifica el archivo del prompt"
        echo "Uso: $0 show <archivo>"
        return 1
    fi
    
    local full_path="$PROMPTS_DIR/$file"
    
    if [ ! -f "$full_path" ]; then
        echo "❌ Error: Archivo no encontrado: $full_path"
        return 1
    fi
    
    echo "📖 Mostrando prompt: $file"
    echo "================================"
    cat "$full_path"
}

create_prompt() {
    local name="$1"
    
    if [ -z "$name" ]; then
        echo "❌ Error: Especifica el nombre del nuevo prompt"
        echo "Uso: $0 create <categoria/nombre>"
        return 1
    fi
    
    local new_file="$PROMPTS_DIR/$name.md"
    local template="$PROMPTS_DIR/templates/prompt_template.md"
    
    if [ ! -f "$template" ]; then
        echo "❌ Error: Plantilla no encontrada: $template"
        return 1
    fi
    
    if [ -f "$new_file" ]; then
        echo "❌ Error: El archivo ya existe: $new_file"
        return 1
    fi
    
    # Crear directorio si no existe
    mkdir -p "$(dirname "$new_file")"
    
    # Copiar plantilla
    cp "$template" "$new_file"
    
    echo "✅ Nuevo prompt creado: $new_file"
    echo "📝 Edita el archivo para personalizar el contenido"
}

# Verificar que existe el directorio de prompts
if [ ! -d "$PROMPTS_DIR" ]; then
    echo "❌ Error: Directorio de prompts no encontrado: $PROMPTS_DIR"
    exit 1
fi

# Procesar comando
case "${1:-help}" in
    "list")
        list_prompts "$2"
        ;;
    "show")
        show_prompt "$2"
        ;;
    "create")
        create_prompt "$2"
        ;;
    "help"|*)
        show_help
        ;;
esac
