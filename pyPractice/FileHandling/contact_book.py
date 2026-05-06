contacts = {}

def show_menu():
	print("\n--- Contact Book Menu ---")
	print("1. Add Contact")
	print("2. View Contact")
	print("3. Search Contact")
	print("4. Edit Contact")
	print("5. Delete Contact")
	print("6. Exit")

def add_contact():
	name = input("Enter contact name : ")
	phone = input("Enter contact phone : ")
	email = input("Enter contact email : ")
	contacts[name] = {"phone":phone, "email":email}
	print(f'{name} has been added to your contacts.')

def view_contacts():
	if contacts:
		print("\n--- Contact List ---")
		for name,details in contacts.items():
			print(f'Name : {name}')
			print(f'Phone : {details["phone"]}')
			print(f'Email : {details["email"]}')
	else:
		print('Your contact book is empty!')

def search_contact():
	name = input('Enter the contact name : ')
	if name in contacts:
		print(f'\n--- Contact Details for {name}---')
		print(f'Name : {name}')
		print(f'Phone : {contacts[name]["phone"]}')
		print(f'Email : {contacts[name]["email"]}')
	else:
		print(f'{name} not found in your contacts!')

def edit_contact():
	name = input('Enter the contact name to edit : ')
	if name in contacts:
		phone = input('Enter new phone number : ')
		email = input('Enter new email address : ')
		contacts[name] = {"phone":phone, "email":email}
		print(f'{name} has been updated!')
	else:
		print(f'{name} not found in your contacts!')

def delete_contact():
	name = input('Enter the contact name to delete : ')
	if name in contacts:
		del contacts[name]
		print(f'{name} has been deleted from your contacts!')
	else:
		print(f'{name} not found in your contacts!')

while True:
	show_menu()
	choice = input('Enter your choice (1-6) : ')
	if choice == '1':
		add_contact()
	elif choice == '2':
		view_contacts()
	elif choice == '3':
		search_contact()
	elif choice == '4':
		edit_contact()
	elif choice == '5':
		delete_contact()
	elif choice == '6':
		print('Exiting Contact Book. Goodbye!')
		break
	else:
		print('Invalid choice! Please enter a number between 1 and 6.')