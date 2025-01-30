def prime():
    number =int(input("enter a number:"))
    if number<=0:
        print("enter number is zero or negative")
        return
    if number==1:
        print("1 is not a prime number.")
        return
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count=count+1

    if count==2:
        print(f"{number} is prime.")
    else:
        print(f"{number} is composite number.")
prime()
