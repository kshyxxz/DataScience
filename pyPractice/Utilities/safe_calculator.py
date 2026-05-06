FILE_NAME = "calculator_log.txt"

def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):	
	if y == 0:
		raise ZeroDivisionError("Cannot divide by zero")
	return x/y

def calculator():
	print("Select operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. Exit")

while True:
	calculator()
	choice = input("Enter choice (1/2/3/4/5): ")

	if choice in ['1', '2', '3', '4', '5']:
		if choice == '5':
			print("Exiting calculator...")
			break
		try:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			if choice == '1':
				print(f"{num1} + {num2} = {add(num1, num2)}")
			elif choice == '2':
				print(f"{num1} - {num2} = {subtract(num1, num2)}")
			elif choice == '3':
				print(f"{num1} * {num2} = {multiply(num1, num2)}")
			elif choice == '4':
				print(f"{num1} / {num2} = {divide(num1, num2)}")
		except ValueError:
				with open(FILE_NAME,"a") as file:
					file.write("Invalid input. Non-numeric value entered.\n")
				print("Invalid input. Please enter a number.")
		except ZeroDivisionError as e:
				with open(FILE_NAME,"a") as file:
					file.write(f"Error: {e}\n")
				print(f"Error: {e}")
		except Exception as e:
				with open(FILE_NAME,"a") as file:
					file.write(f"Unexpected error: {e}\n")
				print(f"An unexpected error occurred: {e}")
		finally:
				with open(FILE_NAME,"a") as file:
					file.write("Operation completed.\n")
				print("Operation completed.\n")
	else:
		print("Invalid choice. Please select a valid operation.")