#!/bin/bash

number=$((RANDOM % 100 + 1))
tries=0
max_tries=5

echo "Guess the number from 1 to 100:"

while [ $tries -lt $max_tries ]; do
    read -p "Your option: " guess
    tries=$((tries + 1))

    if [ "$guess" -eq "$number" ]; then
        echo "Congratulations! You guessed the right number."
        exit 0
    elif [ "$guess" -lt "$number" ]; then
        echo "Too low!"
    else
        echo "Too high!"
    fi

    remaining=$((max_tries - tries))
    if [ $remaining -gt 0 ]; then
        echo "You have $remaining attempts left."
    fi
done

echo "Sorry, you're out of attempts. The correct number was $number."

