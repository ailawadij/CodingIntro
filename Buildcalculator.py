num1 = float(input("Enter first number: "))
# Op is used for an operator like adddition,subtraction, etc
op = input("Enter operator: ")
num2 = float(input("Enter second numer: "))
if op == "+":
    print (num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Error")
