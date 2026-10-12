import random

secret_number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10.")

while attempts < 3:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You win!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"Sorry, you lost. The number was {secret_number}.")


