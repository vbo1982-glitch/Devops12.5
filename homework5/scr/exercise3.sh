#!/bin/bash

read -p "Введіть імя файлу для перевірки: " file
if [ -f "$file" ]; then
    echo "File '$file' exists."
else
    echo "File '$file' does not exist."
fi

