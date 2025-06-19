Num1 = int(input("Enter first number:"))
Num2 = int(input("Enter second number:"))
operation = input("Enter the operation required ( + , - , * , / , % , **) :")
if operation == "+":
    print(Num1+Num2)
elif operation == "-":
    print(Num1-Num2)
elif operation == "*":
    print(Num1*Num2)
elif operation == "/":
    print(Num1/Num2)
elif operation == "%":
    print("Result:", Num1 % Num2)
elif operation == "**":
    print("Result:", Num1 ** Num2)

else:
    print("Error")


