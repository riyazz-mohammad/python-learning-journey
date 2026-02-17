# Program 8: Rock Paper Scissors Game
# Classic game against computer

import random

print("=== ROCK PAPER SCISSORS ===")
print("Choices: rock, paper, scissors")

player = input("Your choice: ").lower()
computer = random.choice(["rock", "paper", "scissors"])

print("\nYou chose:", player)
print("Computer chose:", computer)

if player == computer:
    print("🤝 It's a TIE!")
elif player == "rock":
    if computer == "scissors":
        print("YOU WIN! Rock crushes Scissors!")
    else:
        print("YOU LOSE! Paper covers Rock!")
elif player == "paper":
    if computer == "rock":
        print("YOU WIN! Paper covers Rock!")
    else:
        print("YOU LOSE! Scissors cuts Paper!")
elif player == "scissors":
    if computer == "paper":
        print("YOU WIN! Scissors cuts Paper!")
    else:
        print("YOU LOSE! Rock crushes Scissors!")
else:
    print("Invalid choice! Please enter rock, paper, or scissors!")