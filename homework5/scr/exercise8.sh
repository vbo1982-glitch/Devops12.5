#!/bin/bash

fruits=("apple" "banana" "kiwi" "orange" "mango")

for fruit in "{$fruits[@]}", do
	echo "$fruit"
done


