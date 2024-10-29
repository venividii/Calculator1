def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

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

	 		elif choice == '3':
                	print(f"{num1} * {num2} = {multiply(num1, num2)}")	
        	next_calc = input("Do you want to perform another calculation? (yes/no): ")
        	if next_calc.lower() != 'yes':
	        	break
	     else:
           	 print("Invalid input! Please select a valid operation.")


if __name__ == "__main__":
    calculator()

