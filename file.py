def alisha_calculator():
 print("Simple Calculator")
num1 = int(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter second number: "))
if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")
else:
    print("Invalid operation")