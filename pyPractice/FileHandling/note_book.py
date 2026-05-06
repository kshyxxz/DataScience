FILE_NAME = "myNotes.txt"

def show_menu():
	print("\n--- Note-Taking App Menu ---")
	print("1. Add a new note")
	print("2. View all note(s)")
	print("3. Delete all notes")
	print("4. Exit")

def add_node():
	note = input("Enter your note : ")
	with open(FILE_NAME, "a") as file:
		file.write(note + "\n")
	print("Note added successfully!")

def view_notes():
	try:
		with open(FILE_NAME, "r") as file:
			notes = file.read()
			if notes:
				print("\n--- Your Notes ---")
				print(notes)
			else:
				print("\nNo notes found!")
	except FileNotFoundError:
		print("File doesn't exist.")

def delete_notes():
	confirm = input("Are you sure you want to delete all notes? (Yes/No) : ")
	if confirm.lower() == "yes":
		with open(FILE_NAME, "w") as file:
			pass
		print("All notes have been deleted.")
	else:
		print("Deletion cancelled!")

while True:
	show_menu()
	choice = input("Enter your choice (1-4) : ")

	if choice == "1":
		add_node()
	elif choice == "2":
		view_notes()
	elif choice == "3":
		delete_notes()
	elif choice == "4":
		print("Exiting note taking app...")
		break
	else:
		print("Choose from the 4 options!")