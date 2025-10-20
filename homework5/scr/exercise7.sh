#!/bin/bash

filename=$1
lines=$(wc -l < "$filename")
echo " Number of lines is: $lines"

