def calculator():
  print("Welcome to the calculator!")

  operator = input("Enter an operator (+, -, *, /, *+, +*, quit): \n")

  if operator == "+":
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    result = num1 + num2
    print(round(result, 2))

  elif operator == "-":
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    result = num1 - num2
    print(round(result, 2))

  elif operator == "*":
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    result = num1 * num2
    print(round(result, 2))

  elif operator == "/":
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    if num2 == 0:
      print("Error: Cannot divide by zero")
    else:
      result = num1 / num2
      print(round(result, 2))

  elif operator == "*+":
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    num3 = float(input("Enter the third number: \n"))
    result = num1 * num2 + num3
    print(round(result, 2))

  elif operator == "+*":
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    num3 = float(input("Enter the third number: \n"))
    result = num1 + num2 * num3
    print(round(result, 2))

  elif operator == "quit":
    print("Goodbye!")

  else:
    print(f"{operator} Invalid operator")

#Repeats the program
#Ask user if they want to perform another calculation
  again = input("Do you want to perform another calculation? (y/n): \n")
  if again.lower() == "y":
    calculator()
  elif again.lower() =="n":
      print("Thank you for using the Calculator!")

calculator()
