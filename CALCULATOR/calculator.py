def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero."""
    if y == 0:
        print("Error: Cannot divide by zero.")
        return None
    return x / y

def operate(x, y, operator):
    """Performs the chosen operation on two numbers."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    if operator not in operations:
        print("Invalid operation. Please choose +, -, *, or /.")
        return None
    return operations[operator](x, y)

def main():
    """Prompts user for input, performs calculations, and displays results."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Choose an operation (+, -, *, /): ")
            result = operate(num1, num2, operator)
            if result is not None:
                print("The result is:", result)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        else:
            # Ask if user wants to continue
            choice = input("Do another calculation? (y/n): ")
            if choice.lower() != 'y':
                break

if __name__ == "__main__":
    main()



