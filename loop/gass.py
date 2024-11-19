import random

def guess_with_limit(x):
    random_number = random.randint(1, x)
    attempts = 3  # Set the maximum number of attempts
    for i in range(attempts):
        guess = int(input(f"Attempt {i + 1}/{attempts}: Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again! Too low.")
        elif guess > random_number:
            print("Sorry, guess again! Too high.")
        else:
            print(f"Yay, congrats! You have guessed the number {random_number} correctly.")
            return  # Exit the function once the correct guess is made
    print(f"Sorry, you've used all {attempts} attempts. The number was {random_number}.")

guess_with_limit(10)
