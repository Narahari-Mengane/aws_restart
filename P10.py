# PRogram to print fibonacci series.

num = int(input("Enter Range: "))
v1 = 0
v2 = 1

for i in range(0, num):
    if(i <= 1):
        next = i
    else:
        next = v1 + v2
        v1 = v2
        v2 = next
    print(next)
    