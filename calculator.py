# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Main program
def calculator():
    print("Welcome to the Basic Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. see u next time!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
        else:
            print("Invalid input! Please choose a valid option.")

# Run the calculator
calculator()
