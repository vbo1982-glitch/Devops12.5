#!/bin/bash

echo -n "Enter a sentence: "
read sentence

reversed_sentence=""

for word in $sentence; do 
	reversed_sentence="$word $reversed_sentence"
done

echo "$reversed_sentence"

