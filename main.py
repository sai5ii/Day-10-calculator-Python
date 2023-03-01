from art import logo
from replit import clear

operators = ["+","-","*","/"]
calculations = []

def calculate(num1,operator,num2):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 <= 0:
      return "Divisor must be non zero"
    else:
      return num1 / num2
  else:
    return "Not a valid operation"
def calculator():
  print(logo)
  first_num = float(input(("What's the first number?: ")))
  for operator in operators:
    print(operator)
  should_continue = True
  while should_continue:
    operation = input(("Pick an operation: "))
    second_num = float(input(("What's the next number?: ")))
    answer = calculate(first_num,operation,second_num)
    print(f"{first_num} {operation} {second_num} = {answer}")
    
    if input(f"Type 'y' to continue with {answer}, type 'n' to start a new calculation: ").lower() == 'y':
      first_num = answer
    else:
      clear()
      should_continue = False
      calculator()
    
calculator()  