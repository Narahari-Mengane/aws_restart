# Python program to find the factorial of a number provided by the user.

num = int(input("Enter Number: "))

factorial = 1

if num < 0:
    print("Invalid Number")
else:
    for i in range(1, num+1):
        factorial =factorial * i
    print("The Factorial of ", num, "is", factorial)
