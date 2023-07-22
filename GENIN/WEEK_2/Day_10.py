# Day_10
# Calculator_project

def add (n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 + (n2 * -1)
def multiply(n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1/n2

operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide}
def calc():
    going = True
    while going:
        num1 = float(input("What is your first number "))
        for ke in operation:
            print(f"{ke}")

        operation_symbol = input("pick an operation: ")
        num2 = float(input("What is the next number "))
        drey = operation[operation_symbol]
        
        first_answer = drey(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        decision = input(f"type 'y' to continue calculating with {first_answer}, or type 'n' to exit").lower()
        if decision != "y":
            going = False
calc()