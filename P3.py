# Python program to swap two variables

n1 = float(input("Enter 1st Value: "))
n2 = float(input("Enter 2nd Value: "))
print("\n***Before Swapping***")
print("1st Value: ",n1)
print("2nd vlaue: ",n2)

n1, n2 = n2, n1

print("\n***After Swapping***")
print("1st Value: ",n1)
print("2nd vlaue: ",n2)
