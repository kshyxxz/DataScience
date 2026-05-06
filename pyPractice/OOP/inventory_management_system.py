class Inventory:
	total_items = 0

	def __init__(self, product_name, price, quantity):
		self.product_name = product_name
		self.price = price
		self.quantity = quantity
		Inventory.total_items += quantity

	def show_product_details(self):
		print(f"Product Name: {self.product_name}")
		print(f"Price: ${self.price}")
		print(f"Quantity: {self.quantity}")

	def sell_product(self, amount):
		if amount > self.quantity:
			print("Not enough stock to sell.")
		else:
			self.quantity -= amount
			Inventory.total_items -= amount
			print(f"Sold {amount} units of {self.product_name}.")
		
	@staticmethod
	def calculate_discounted_price(price, discount_percentage):
		return price - (price * discount_percentage / 100)
	
	@classmethod
	def get_total_items(cls):
		print(f"Total items in inventory: {Inventory.total_items}")
	
products = []

def add_product():
	product_name = input("Enter product name: ")
	price = float(input("Enter product price: "))
	quantity = int(input("Enter product quantity: "))
	products.append(Inventory(product_name, price, quantity))
	print(f"{quantity} units of {product_name} added to inventory.")

def view_products():
	if not products:
		print("No products in inventory.")
	else:
		for product in products:
			product.show_product_details()
			print("-" * 20)

def sell_product():
	product_name = input("Enter product name to sell: ")
	amount = int(input("Enter quantity to sell: "))
	for product in products:
		if product.product_name == product_name:
			product.sell_product(amount)
			return
	print("Product not found in inventory.")

def calculate_discount():
	price = float(input("Enter product price: "))
	discount_percentage = float(input("Enter discount percentage: "))
	discounted_price = Inventory.calculate_discounted_price(price, discount_percentage)
	print(f"Discounted Price: ${discounted_price:.2f}")

while True:
	print("\nInventory Management System")
	print("1. Add Product")
	print("2. View Products")
	print("3. Sell Product")
	print("4. Calculate Discounted Price")
	print("5. Total Items in Inventory")
	print("6. Exit\n")

	choice = input("Enter your choice: ")

	if choice == '1':
		add_product()
	elif choice == '2':
		view_products()
	elif choice == '3':
		sell_product()
	elif choice == '4':
		calculate_discount()
	elif choice == '5':
		Inventory.get_total_items()
	elif choice == '6':
		print("Exiting the system.")
		break
	else:
		print("Invalid choice. Please try again.")