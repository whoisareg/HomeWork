import math 
    
def logarithm(x):
    return math.log(x)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangens(x):
    return math.tan(x)

def cotangens(x):
    return 1 / math.tan(x)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def square_root(x):
    return math.sqrt(x)

def print_menu():
    print("Choose the operation:")
    print("1. Logarithm (base e)")
    print("2. Sine")
    print("3. Cosine")
    print("4. Tangens")
    print("5. Cotangens")
    print("6. Factorial")
    print("7. Square Root")
    print("0. Exit")

def get_valid_choice():
    while True:
        choice = input("Enter your choice: ")
        if choice in ['0', '1', '2', '3', '4', '5', '6', '7']:
            return choice
        else:
            print("Invalid choice. Please enter a valid option.")

while True:
    print_menu()
    choice = get_valid_choice()

    if choice == '0':
        print("Exiting the program.")
        break
    elif choice == '1':
        x = float(input("Enter the number: "))
        print("Result:", logarithm(x))
    elif choice == '2':
        x = float(input("Enter the number (in radians): "))
        print("Result:", sine(x))
    elif choice == '3':
        x = float(input("Enter the number (in radians): "))
        print("Result:", cosine(x))
    elif choice == '4':
        x = float(input("Enter the number (in radians): "))
        print("Result:", tangens(x))
    elif choice == '5':
        x = float(input("Enter the number (in radians): "))
        print("Result:", cotangens(x))
    elif choice == '6':
        x = int(input("Enter the number: "))
        print("Result:", factorial(x))
    elif choice == '7':
        x = float(input("Enter the number: "))
        print("Result:", square_root(x))
