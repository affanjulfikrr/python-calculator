# calculator_menu.py
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    clear_screen()
    print("┌─────────────────────────────┐")
    print("│     AFFAN's Calculator      │")
    print("└─────────────────────────────┘")
    print("  1. Addition       2. Subtraction")
    print("  3. Multiplication 4. Division")
    print("  5. Exit")
    print("───────────────────────────────")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("\nThank you for using!")
        return False

    if choice not in ['1','2','3','4']:
        print("Invalid choice!")
        input("\nPress Enter to continue...")
        return True

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Numbers only.")
        input("\nPress Enter...")
        return True

    if choice == '1':
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"\nResult: {num1} × {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("\nError: Division by zero!")
        else:
            print(f"\nResult: {num1} ÷ {num2} = {num1 / num2}")

    input("\nPress Enter to continue...")
    return True

while calculator():
    pass