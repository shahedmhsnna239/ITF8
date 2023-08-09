import math

def sum_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_rectangle_area(length, width):
    return length * width

def main():
    while True:
        print("Main Menu:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Calculate triangle area")
        print("6. Calculate circle area")
        print("7. Calculate rectangle area")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '8':
            print("Exiting the program.")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = sum_numbers(num1, num2)
            elif choice == '2':
                result = subtract_numbers(num1, num2)
            elif choice == '3':
                result = multiply_numbers(num1, num2)
            elif choice == '4':
                result = divide_numbers(num1, num2)
            elif choice == '5':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                result = calculate_triangle_area(base, height)
            elif choice == '6':
                radius = float(input("Enter the radius of the circle: "))
                result = calculate_circle_area(radius)
            elif choice == '7':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                result = calculate_rectangle_area(length, width)

            print("Result:", result)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
