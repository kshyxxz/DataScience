def celsius_to_fahrenheit(celsius):
	return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
	return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
	return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
	return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
	return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
	print("\n--- Temperature Converter ---")
	print("1. Celsius to Fahrenheit")
	print("2. Celsius to Kelvin")
	print("3. Fahrenheit to Celsius")
	print("4. Fahrenheit to Kelvin")
	print("5. Kelvin to Celsius")
	print("6. Kelvin to Fahrenheit")
	print("7. Exit")

while True:
	temperature_converter()
	choice = input("Enter choice (1/2/3/4/5/6/7): ")

	if choice in ['1', '2', '3', '4', '5', '6', '7']:
		if choice == '7':
			print("Exiting temperature converter...")
			break
		try:
			temp = float(input("Enter temperature: "))
			if choice == '1':
				print(f"{temp} °C = {celsius_to_fahrenheit(temp):.2f} °F")
			elif choice == '2':
				print(f"{temp} °C = {celsius_to_kelvin(temp):.2f} K")
			elif choice == '3':
				print(f"{temp} °F = {fahrenheit_to_celsius(temp):.2f} °C")
			elif choice == '4':
				print(f"{temp} °F = {fahrenheit_to_kelvin(temp):.2f} K")
			elif choice == '5':
				print(f"{temp} K = {kelvin_to_celsius(temp):.2f} °C")
			elif choice == '6':
				print(f"{temp} K = {kelvin_to_fahrenheit(temp):.2f} °F")
		except ValueError:
				print("Invalid input. Please enter a numeric value.")
	else:
		print("Invalid choice. Please select a valid option.")