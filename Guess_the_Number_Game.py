import random  # for generating random numbers

print("🎉 Welcome to Guess the Number Game! 🎉")
print("I have selected a number between 1 and 100. Can you guess it?")

play_again = "yes"

while play_again.lower() == "yes":
    number_to_guess = random.randint(1, 100)  # generate random number
    guess = 0
    attempts = 0  # count the number of guesses

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1  # increase attempt count

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You've guessed the number in {attempts} attempts! 🎯")
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 100.")
    
    play_again = input("Do you want to play again? (yes/no): ")