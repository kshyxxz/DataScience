class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.is_borrowed = False
		
	def display_info(self):
		status = "Available" if not self.is_borrowed else "Borrowed"
		print(f'\nTitle : {self.title}')
		print(f'Author : {self.author}')
		print(f'Status : {status}\n')

class Library:
	def __init__(self):
		self.books = []

	def add_book(self, title, author):
		new_book = Book(title,author)
		self.books.append(new_book)
		print(f'Book {title} by {author} added to the library.')

	def view_books(self):
		if not self.books:
			print('No books in the library')
		else:
			print('Library Books : ')
			for book in self.books:
				book.display_info()
				
	def borrow_book(self,title):
		for book in self.books:
			if book.title == title and not book.is_borrowed:
				book.is_borrowed = True
				print(f'The book {title} has been borrowed')
				return
		print(f'Book currently not available')

	def return_book(self,title):
		for book in self.books:
			if book.title == title and book.is_borrowed:
				book.is_borrowed = False
				print(f'Book {title} has been returned')
				return
		print(f'Book {title} is not in the library')
	
library = Library()

while True:
	print("\nLibrary Management System")
	print("1. Add Book")
	print("2. View Books")
	print("3. Borrow Book")
	print("4. Return Book")
	print("5. Exit\n")

	choice = int(input("Enter your choice : "))
	if choice == 1:
		title = input("Enter book title : ")
		author = input("Enter book author : ")
		library.add_book(title, author)
	elif choice == 2:
		library.view_books()
	elif choice == 3:
		title = input("Enter book title to borrow : ")
		library.borrow_book(title)
	elif choice == 4:
		title = input("Enter book title to return : ")
		library.return_book(title)
	elif choice == 5:
		print("Exiting...")
		break
	else:
		print("Invalid choice! Please try again.")