
#! PROJECT 2 – THE PERFECT GUESS

# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

computer = random.randint(0, 50)

guess = int(input("Enter your guess : "))

attempt = 0

while guess != computer:
    if guess > computer:
        print("Guess is greater than the computer's number.")

    elif guess < computer:
        print("Guess is lower than the computer's number.")

    attempt += 1
    guess = int(input("Enter your guess : "))

print(f"Congrats! Your guess was the right one done in {attempt}!")
