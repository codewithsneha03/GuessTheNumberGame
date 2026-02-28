import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("🎮 Welcome to Rock Paper Scissors!")
print("First to 3 wins the game!")
print("-" * 40)

while user_score < 3 and computer_score < 3:
    
    user = input("Enter rock, paper or scissors: ").lower()
    
    # ❌ Invalid input handling
    if user not in choices:
        print("⚠ Invalid choice! Please try again.\n")
        continue
    
    computer = random.choice(choices)
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    # 🧠 Game Logic
    if user == computer:
        print("🤝 It's a tie!")
        
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("✅ You win this round!")
        user_score += 1
        
    else:
        print("❌ Computer wins this round!")
        computer_score += 1
    
    # 🧮 Score display
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
    print("-" * 40)

# 🏆 Final Winner
if user_score == 3:
    print("🎉 Congratulations! You won the game!")
else:
    print("💻 Computer won the game. Better luck next time!")