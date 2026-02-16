recipe_ingredients = {"flour", "sugar", "eggs", "milk", "butter"}

user_input = input("Enter the ingredients you have (separated by commas) : ")
user_ingredients = set(user_input.split(","))

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients = recipe_ingredients

print("\n--- Ingredient Check Result ---")
if missing_ingredients:
	print(f"You are missing these ingredients : {','.join(missing_ingredients)}.")
else:
	print(f"You have all the ingredients needed.")