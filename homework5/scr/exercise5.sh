#!/bin/bash
# Exercise 5

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <source> <destination>"
  exit 2
fi
src="$1"
dst="$2"
if [ ! -e "$src" ]; then
  echo "Source '$src' does not exist." >&2
  exit 1
fi
cp -v -- "$src" "$dst"	
