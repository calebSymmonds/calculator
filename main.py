from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  cont = True
  
  while cont == True:
    reply = input("Continue? (yes or no)\n").lower()
    if reply == "no":
      cont = False
      print("K. Bye.")
      break
    operation_symbol = input("Pick another operation: ") 
    num3 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol] 
    second_answer = calculation_function(calculation_function(num1, num2), num3)
    second_answer = calculation_function(first_answer, num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

calculator()
