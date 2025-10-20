#!bin/bash

filename=$1
lines=$(wc -1 < "$filename")
echo " Number of lines is: $lines"

