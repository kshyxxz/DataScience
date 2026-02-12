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
			print(f'Phone : {details['phone']}')
			print(f'Email : {details['email']}')
	else:
		print('Your contact book is empty!')

def search_contact():
	name = input('Enter the contact name!')
	if name in contacts:
		print(f'\n--- Contact Details for {name}---')
		print(f'Name : {name}')
		print(f'Phone : {contacts[name]['phone']}')
		print(f'Name : {contacts[name]['email']}')