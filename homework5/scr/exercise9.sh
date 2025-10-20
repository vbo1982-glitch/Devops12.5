#!/bin/bash

echo -n "Enter filename: "
read filename

if [ -f "$filename" ]; then
	cat "$filename"
else
	echo "file does no exists!!!!!"
fi	

