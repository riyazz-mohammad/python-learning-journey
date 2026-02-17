# Program 5: Number Guessing Game
# Player guesses a number between 1-100

import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("=== NUMBER GUESSING GAME ===")
print(f"Guess the number between 1-100!")
print(f"You have {max_attempts} attempts!\n")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: Enter guess: "))
    attempts += 1

    if guess == secret:
        print(f"\n🎉 CORRECT! The number was {secret}!")
        print(f"You got it in {attempts} attempts!")
        if attempts <= 3:
            print("🏆 INCREDIBLE! You're a genius!")
        elif attempts <= 5:
            print("👍 Great job!")
        else:
            print("😅 Made it just in time!")
        break
    elif guess < secret:
        remaining = max_attempts - attempts
        print(f"📈 Too LOW! Go higher! ({remaining} attempts left)")
    else:
        remaining = max_attempts - attempts
        print(f"📉 Too HIGH! Go lower! ({remaining} attempts left)")
else:
    print(f"\n💀 GAME OVER! The number was {secret}!")
    print("Better luck next time!")