from datetime import datetime
JOURNAL_FILE = '../dailty_journal.txt'

def add_emtry():
	entry = input("Write your journal entry : ")
	with open(JOURNAL_FILE, 'a') as file:
		file.write(entry + '\t' + str(datetime.now()) + '\n')
	print("Entry added successfully!")

def view_entries():
	try:
		with open(JOURNAL_FILE, 'r') as file:
			content = file.read()
			if content:
				print("--- Your Journal Entries ---")
				print(content)
			else:
				print("No entries found. Start writing today")
	except FileNotFoundError:
		print("No journal file found. Add an entry first!")

def search_entries():
	keyword = input("Enter a keyword to search for : ").lower()
	try:
		with open(JOURNAL_FILE, 'r') as file:
			entries = file.readlines()
			found = False
			print("Search Results")
			for entry in entries:
				if keyword in entry.lower():
					print(entry.strip())
					found = True
			if not found:
				print("No matching entries found")
	except FileNotFoundError:
		print("No journal file found. Add an entry first!")

def show_menu():
	print("\n--- Journal Logger ---")
	print("1. Add Entry")
	print("2. View Entries")
	print("3. Search Entries")
	print("4. Exit")

while True:
	show_menu()
	choice = input("Choose an option (1-4) : ").strip()
	if choice == '1':
		add_emtry()
	elif choice == '2':
		view_entries()
	elif choice == '3':
		search_entries()
	elif choice == '4':
		print("Exiting the journal logger. Goodbye!")
		break
	else:
		print("Invalid choice. Please select a valid option.")