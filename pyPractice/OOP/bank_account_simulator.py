class BankAccount:
	def __init__(self, account_holder, balance = 0):
		self.account_holder = account_holder
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f'Deposited {amount}. New balance: {self.balance}')
		else:
			print('Amount must be greater then 0!')

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			print(f'Withdrawn {amount}. New balanceL {self.balance}')
		else:
			print('Insuffecient funds!')
	
	def show_details(self):
		print(f'Account holder: {self.account_holder} \nBalance: {self.balance}')

accounts = {}

def create_account():
	name = input('Enter account holders name : ').strip()
	initial_balance = input('Enter the initial balance : ')
	account = BankAccount(name, initial_balance)
	accounts[name] = account
	print('Account created successfully!')

def access_account():
	name = input('Enter account holders name : ').strip()
	if name in accounts:
		account = accounts[name]
		while True:
			print('\n1. Deposit')
			print('2. Withdraw')
			print('3. Show details')
			print('4. Exit\n')
			choice = int(input('Enter an option : '))

			if choice == 1:
				amount = float(input('Enter the deposit amount : '))
				account.deposit(amount)
			elif choice == 2:
				amount = float(input('Enter the withdraw amount : '))
				account.withdraw(amount)
			elif choice == 3:
				account.show_details()
			elif choice == 4:
				print(f'Exitinggg...')
				break
			else:
				print('Invalid choice!')
	else:
		print(f'Account not found!')

while True:
	print('\n--- Bank Account Simulator ---')
	print('1. Create Account')
	print('2. Access Account')
	print('3. Exit\n')
	choice = int(input('Enter your choice : '))
	
	if choice == 1:
		create_account()
	elif choice == 2:
		access_account()
	elif choice == 3:
		print(f'Exiting..')
		break
	else:
		print('Enter valid option!')
