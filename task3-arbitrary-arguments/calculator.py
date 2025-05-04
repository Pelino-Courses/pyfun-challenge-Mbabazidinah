def add(*args):
    """Return the sum of all arguments."""
    return sum(args)

def multiply(*args):
    """Return the product of all arguments."""
    result = 1
    for arg in args:
        result *= arg
        return result

def subtract(*args):
    """Return the result of subtracting all arguments from the first."""
    if len(args) == 0:
        return 0
    result = args[0]
    for arg in args[1:]:
        result -= arg
    return result

def divide(*args):
    """Return the result of dividing the first argument by all subsequent arguments."""
    if len(args) == 0:
        return 0
    result = args[0]
    for arg in args[1:]:
        if arg == 0:
            raise ValueError("division by zero is not allowed")
        result /= arg
    return result

def exponentiate(*args):
    """Return the result of raising the first argument to the power of all subsequent arguments."""
    if len(args) == 0:
        return 1
    result = args[0]
    for arg in args[1:]:
        result **= arg
    return result

def calculator(*args, **kwargs):
    """Perform the specified operation on the given arguments."""
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError("All arguments must be numbers")
    if len(args) == 0:
        raise ValueError("At least one argument is required")
    operation = kwargs.get("operation")
    if operation == "add":
        return add(*args)
    elif operation == "multiply":
        return multiply(*args)
    elif operation == "subtract":
        return subtract(*args)
    elif operation == "divide":
        return divide(*args)
    elif operation == "exponentiate":
        return exponentiate(*args)
    else:
        raise ValueError("Invalid operation")

if __name__ == "__main__":
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        number3 = int(input("Enter the third number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide, exponentiate): ")
        result = calculator(number1, number2, number3, operation=operation)
        print(f"The result of {operation} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
