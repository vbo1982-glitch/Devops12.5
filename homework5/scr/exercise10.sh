#!/bin/bash/

mkdir -p ~/watch

while true; do

    for file ~/watch/*; do
        if [[ "$file" == *.back ]]; then
		continue
	elif [[ -f "$file" ]]; then
		cat "$file"
		mv "$file" "$file.back"
        fi
    done
    sleep 5
gone
