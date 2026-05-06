class BankAccount:
	def __init__(self, account_number, pin, balance=0):
		self.account_number = account_number
		self.__pin = pin
		self.__balance = balance

	def validate_pin(self, entered_pin):
		return entered_pin == self.__pin
	
	def check_balance(self):
		print(f'Current Balance : {self.__balance}')

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print(f'Deposited : {amount}. New Balance is : {self.__balance}')
		else:
			print('Invalid amount!')

	def withdraw(self, amount):
		if amount > 0:
			if amount > self.__balance:
				print('Insufficient funds!')
			else:
				self.__balance -= amount
				print(f'Withdrawn : {amount}. New Balance is : {self.__balance}')
		else:
			print('Invalid amount!')
	
	def change_pin(self, old_pin, new_pin):
		if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigits():
			self.__pin = new_pin
			print('Pin changed successfully!')
		else:
			print('Pin change unsuccessful!!')

class ATM:
	def __init__(self):
		self.accounts = {}

	def create_account(self):
		account_number = input('Enter account number : ')
		pin = input('Set a 4-digit PIN : ')
		if len(pin) == 4 and pin.isdigit():
			self.accounts[account_number] = BankAccount(account_number, pin)
			print('Account created successfully!')
		else:
			print('Invalid PIN!')

	def authenticate_account(self):
		account_number = input('Enter the account number : ')
		pin = input('Enter PIN : ')

		account = self.accounts.get(account_number)
		if account and account.validate_pin(pin):
			print('Authentication Successful!')
			self.account_menu(account)
		else:
			print('Invalid account number or PIN!')

	def account_menu(self,account):
		while True:
			print('\n1. Check Balance')
			print('2. Deposit')
			print('3. Withdraw')
			print('4. Change PIN')
			print('5. Exit')
			choice = input('Enter your choice : ')

			if choice == '1':
				account.check_balance()
			elif choice == '2':
				amount = float(input('Enter the amount to deposit : '))
				account.deposit(amount)
			elif choice == '3':
				amount = float(input('Enter the amount to withdraw : '))
				account.withdraw(amount)
			elif choice == '4':
				old_pin = input('Enter the current PIN : ')
				new_pin = input('Enter the new 4-digit PIN : ')
				account.change_pin(old_pin, new_pin)
			elif choice == '5':
				print('Thank you for using our ATM!')
				break
			else:
				print('Invalid choice! Please try again.')
			
if __name__ == "__main__":
	atm = ATM()
	while True:
		print('\n1. Create Account')
		print('2. Access Account')
		print('3. Exit')
		main_choice = input('Enter your choice : ')

		if main_choice == '1':
			atm.create_account()
		elif main_choice == '2':
			atm.authenticate_account()
		elif main_choice == '3':
			print('Goodbye!')
			break
		else:
			print('Invalid choice! Please try again.')