import random 
  
def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    print("У вас є 5 спроб вгадати число від 1 до 100.")
    while attempts < max_attempts:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            return
    print(f"На жаль, спроби закінчилися. Загадане число було {number_to_guess}.")

if __name__ == "__main__":
    guess_number()