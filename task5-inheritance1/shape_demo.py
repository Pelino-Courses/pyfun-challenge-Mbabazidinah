from shape import Circle, Rectangle, Triangle

def get_positive_number(prompt):
    """
    Prompt the user for a positive number, retrying if the input is invalid.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        float: A valid positive number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_shape():
    """
    Prompts the user to choose a shape and creates it based on user input.

    Returns:
        Shape: An instance of Circle, Rectangle, or Triangle.
    """
    options = {
        "1": "Circle",
        "2": "Rectangle",
        "3": "Triangle"
    }

    print("Shape Selection:")
    for key, name in options.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            radius = get_positive_number("Enter the radius: ")
            return Circle(radius)
        elif choice == "2":
            width = get_positive_number("Enter the width: ")
            height = get_positive_number("Enter the height: ")
            return Rectangle(width, height)
        elif choice == "3":
            base = get_positive_number("Enter the base: ")
            height = get_positive_number("Enter the height: ")
            return Triangle(base, height)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    """
    Main loop for creating and displaying shapes.
    """
    print("Welcome to the Shape Creator!")

    while True:
        shape = choose_shape()
        print("\nShape Details:")
        print(shape)

        again = input("\nWould you like to create another shape? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
