class UserProfile:
	def __init__(self,username,email,password):
		self.username = username
		self._email = email
		self.__password = password
		self.set_password(password)

	def get_email(self):
		return self._email
	
	def set_email(self, new_email):
		if '@' in new_email and '.' in new_email:
			self._email = new_email
			print('Email set successful!')
		else:
			print('Format invalid!')
		
	def set_password(self, new_password):
		if len(new_password) > 8:
			self.__password = new_password
			print('Password set successfully!')
		else:
			print('Password length should be greater than 8!')
	
	def display_profile(self):
		print('\nUser Profile : ')
		print(f'Username : {self.username}')
		print(f'Email : {self._email}')
		print(f'Password : {self.__password}')

users = []

def create_user():
	username = input('Enter the username : ')
	for user in users:
		if user.username == username:
			print('Username already exists!')
			return
	email = input('Enter the email : ')
	password = input('Enter the password : ')
	users.append(UserProfile(username,email,password))
	print('User created successfully!')

def view_users():
	if not users:
		print('No users found!')
	else:
		for user in users:
			user.display_profile()

def update_email():
	username = input('Enter the username to update : ')
	for user in users:
		if user.username == username:
			new_email = input('Enter the new email : ')
			user.set_email(new_email)
			return
	print('User not found!')

def update_password():
	username = input('Enter the username to update : ')
	for user in users:
		if user.username == username:
			new_password = input('Enter the new password : ')
			user.set_password(new_password)
			return
	print('User not found!')

while True:	
	print('\n1. Create User')
	print('2. View Users')
	print('3. Update Email')
	print('4. Update Password')
	print('5. Exit')

	choice = int(input('Enter your choice : '))
	if choice == 1:
		create_user()
	elif choice == 2:
		view_users()
	elif choice == 3:
		update_email()
	elif choice == 4:
		update_password()
	elif choice == 5:
		print('Exiting the program!')
		break
	else:
		print('Enter valid option!')