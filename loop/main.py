import random

def guss(x):
    random_number = random.randint(1,x)
    guss = 0
    while guss !=random_number:
        guss=int(input(f"Guss a number between 1 and {x}:"))
        if guss < random_number:
            print("Sorry,guess again!. Too low")
        elif guss >random_number:
            print("Sorry,guess again!. Too high")
        

    print(f"Yay, congrats you have gussed the number {random_number}")
guss(10)