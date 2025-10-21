#!/bin/bash


WATCH_DIR="$HOME/watch"

mkdir -p "$WATCH_DIR"
echo "Моніторинг директорії: $WATCH_DIR (кожні 5 секунд)"

while true; do

    for file in "$WATCH_DIR"/*; do
        
            if [ ! -e "$file" ]; then
            continue
        fi

        if [[ "$file" == *.back ]]; then
            continue
        
        elif [[ -f "$file" ]]; then
            echo "----------------------------------------"
            echo "✅ Знайдено новий файл: $file"
            echo "Вміст:"
            
            cat "$file"
            
            mv "$file" "$file.back"
            echo "Перейменовано на: $file.back"
            echo "----------------------------------------"
        fi
    done
   
    sleep 5
    
done
