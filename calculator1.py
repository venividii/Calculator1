def add(x, y):


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

       	    next_calc = input("Do you want to perform another calculation? (yes/no): ")
            if next_calc.lower() != 'yes':
                break

if __name__ == "__main__":
    calculator()
