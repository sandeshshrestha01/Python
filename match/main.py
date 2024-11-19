def calculator():
    print("select operator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4. Division (/)")

    operator= input("Enter a Operator (+,-,*,/):")
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    match operator:
        case '+':
            print(f"Sum of {num1}+{num2}={num1+num2}")
        case '-':
            print(f"Different of {num1}-{num2}={num1 - num2}")
        case '*':
            print(f"Multiplication of {num1}*{num2}={num1 * num2}")
        case '/':
            if num2!=0:
                print(f"Division of {num1}/{num2}={num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")


        case _ :
            print("Invalid Operator! please select(+,-,*,/) ")
calculator()
