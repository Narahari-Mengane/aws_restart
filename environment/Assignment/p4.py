# Program to check if a number is prime or not

num = int(input("Enter Number: "))
flag = False

if num == 1:
    print("Number is not Prime")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    
    if flag:
        print(num, "is not Prime")
    else:
        print(num, "is prime")
        