import random

def computer_guess(x):
    low = 1
    high = x
    attemps=3
    for i in range(attemps):
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one option left
        feedback = input(f" attemps {i+1}/{attemps}:Is {guess} is too high(h), too low(l) or corrects(c)")
        if feedback =='c':
            print(f"Yay! The computer guessed your number {guess} correctly.")
        elif feedback=='h':
            high=guess-1
        elif feedback =='l':
            low= guess+1
        else:
            pass
    print("Sorry, the computer couldn't guess your number within the allowed attempts.") 

computer_guess(10)       
