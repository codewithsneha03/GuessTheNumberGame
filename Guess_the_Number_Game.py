import random

number_to_guess = random.randint(1,100)
print("Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

guess = 0

while guess != number_to_guess:
    try:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")