# try:
    #code that may cause exception
# except:
    #code to run when exception occurs
from multiprocessing.reduction import recvfds

try:
    even_number=[2,4,6,8]
    print(even_number[0])
except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index out of Bound.")

# try:
#     num1=10
#     num2=3
#     result = num1/num2
#     print(result)
# except:
#     print("Error: Denominator cannot be 0")
#
#  finally:
#      print("this is finally block")

try:
    num1=10
    num2=0

    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be 0")

try:
    num=int(input("enter a number:"))
    assert num%2==0
    print("even number")
except:
    print("not an even number")

else:
    reciprocal=1/num
    print(reciprocal)