def load_recipes(file_path):
	try:
		with open(file_path, 'r') as file:
			content = file.read()
			recipes = content.split('\n\n')  
			recipe_dict = {}
			for recipe in recipes:
				lines = recipe.split('\n')
				if len(lines) >= 3:
					name = lines[0].strip()
					ingredients = lines[1].replace('Ingredients: ', '').strip()
					instructions = lines[2].replace('Instructions: ', '').strip()
					recipe_dict[name] = {
						'ingredients': ingredients,
						'instructions': instructions
					}
			return recipe_dict
	except FileNotFoundError:
		print(f"Error: The file '{file_path}' was not found.")
		return {}
	
def show_menu():
	print("\nRecipe Viewer Menu:")
	print("1. View all recipes")
	print("2. View a specific recipe")
	print("3. Exit")

def view_recipes(recipes):
	name = input("Enter the name of the recipe you want to view: ").strip()
	if name in recipes:
		print(f"\nRecipe: {name}")
		print(f"Ingredients: {recipes[name]['ingredients']}")
		print(f"Instructions: {recipes[name]['instructions']}")
	else:
		print(f"Recipe '{name}' not found.")

recipe_file = '../recipes.txt'
recipes = load_recipes(recipe_file)

while True:
	show_menu()
	choice = input("Enter your choice: ").strip()
	if choice == '1':
		print("\nAvailable Recipes:")
		for recipe_name in recipes.keys():
			print(f"- {recipe_name}")
	elif choice == '2':
		view_recipes(recipes)
	elif choice == '3':
		print("Exiting the Recipe Viewer. Goodbye!")
		break
	else:
		print("Invalid choice. Please try again.")