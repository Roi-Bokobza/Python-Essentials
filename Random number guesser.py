import random
import time

score = 0

while True:
    time.sleep(1)
    difficulty = input(f"\nWelcome to guess the number! Choose your difficulty level \n(e)asy\n(m)edium\n(h)ard\n\nYour current score is {score}\n\nChoose a difficulty: ").strip().lower()

    if difficulty not in ['e', 'm', 'h']:
        print("\nInvalid option, please choose again.")
        continue

    ##################################### Easy difficulty

    if difficulty == "e":
        num = random.randint(1, 10)
        attempts = 5
        print("Chosen Difficulty: Easy")
        time.sleep(1)

        while attempts > 0:
            guess = input(f"\nYou have {attempts} attempts left.\nGuess a number between 1 and 10: ")

            if guess == "r":
                print("\nReturning to main menu...")
                break

            guess = int(guess)

            if guess < 1 or guess > 10:
                print("\nGuess is out of range. Please enter a number between 1 and 10.")
                continue

            if guess < num:
                print("Too low.")
            elif guess > num:
                print("Too high.")
            else:
                score += 5
                print(f"\nCongratulations! You guessed it!, your total score is {score}")
                break

            attempts -= 1

        if attempts == 0:
            print(f"\nOut of attempts! The correct number was {num}.")

    ################################# Medium Difficulty

    elif difficulty == "m":
        num = random.randint(1, 30)
        attempts = 5
        print("Chosen Difficulty: Medium")
        time.sleep(1)

        while attempts > 0:
            guess = input(f"\nYou have {attempts} attempts left.\nGuess a number between 1 and 30: ")

            if guess == "r":
                print("\nReturning to main menu...")
                break

            guess = int(guess)

            if guess < 1 or guess > 30:
                print("\nGuess is out of range. Please enter a number between 1 and 30.")
                continue

            if guess < num:
                print("Too low.")
            elif guess > num:
                print("Too high.")
            else:
                score += 10
                print(f"\nCongratulations! You guessed it!, your total score is {score}")
                break

            attempts -= 1

        if attempts == 0:
            print(f"\nOut of attempts! The correct number was {num}.")

    ################################### Hard difficulty

    elif difficulty == "h":
        num = random.randint(1, 100)
        attempts = 10
        print("Chosen Difficulty: Hard")
        time.sleep(1)

        while attempts > 0:
            guess = input(f"\nYou have {attempts} attempts left.\nGuess a number between 1 and 100: ")

            if guess == "r":
                print("\nReturning to main menu...")
                break

            guess = int(guess)

            if guess < 1 or guess > 100:
                print("\nGuess is out of range. Please enter a number between 1 and 100.")
                continue

            if guess < num:
                print("Too low.")
            elif guess > num:
                print("Too high.")
            else:
                score += 20
                print(f"\nCongratulations! You guessed it!, your total score is {score}")
                break

            attempts -= 1

        if attempts == 0:
            print(f"\nOut of attempts! The correct number was {num}")
