a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a ^ b
b = a ^ b
a = a ^ b
print("first number: ", a, "\n", "second number: ", b)
