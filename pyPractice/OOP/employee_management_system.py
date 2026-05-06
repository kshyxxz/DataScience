class Employee:
	def __init__(self,name,emp_id,salary):
		self.name = name
		self.emp_id = emp_id
		self.salary = salary

	def display_info(self):
		print(f'Employee details of id {self.emp_id} :')
		print(f'Name : {self.name}')
		print(f'Salary : {self.salary}')
	
	def calculate_bonus(self):
		bonus = 0.1 * self.salary
		print(f'Bonus on employee with id {self.emp_id} : {bonus}')

class Manager(Employee):
	def __init__(self, name, emp_id, salary, department):
		super().__init__(name, emp_id, salary)
		self.department = department

	def display_info(self):
		super().display_info()
		print(f'Department : {self.department}')

	def calculate_bonus(self):
		bonus = 0.2 * self.salary
		print(f'Bonus on employee with id {self.emp_id} : {bonus}')

class Developer(Employee):
	def __init__(self, name, emp_id, salary,programming_language):
		super().__init__(name, emp_id, salary)
		self.programming_language = programming_language

	def display_info(self):
		super().display_info()
		print(f'Programmming Language : {self.programming_language}')
	
	def calculate_bonus(self):
		bonus = 0.5 * self.salary
		print(f'Bonus on employee with id {self.emp_id} : {bonus}')
		
employees = []

def add_employee():
	print(f'Enter the type of employee you want to add : ')
	print('1. General Employee')
	print('2. Manager')
	print('3. Developer')
	choice = int(input('Enter your choice : '))

	emp_id = int(input('Enter employee id : '))
	name = input('Enter employee name : ')
	salary = float(input('Enter employee salary : '))
	if choice == 1:
		employees.append(Employee(name,emp_id,salary))
		print('General employee added successfully!')
	elif choice == 2:
		department = input('Enter department name : ')
		employees.append(Manager(name,emp_id,salary,department))
		print('Manager employee added successfully!')
	elif choice == 3:
		programming_language = input('Enter the programming language : ')
		employees.append(Developer(name,emp_id,salary,programming_language))
		print('Developer employee added successfully!')
	else:
		print('Enter valid option!')
		return
	
def employee_details():
	if len(employees) > 0:
		for employee in employees:
			print(f'\nEmployee Id : {employee.emp_id}')
			print(f'Employee Name : {employee.name}')
			print(f'Employee Salary : {employee.salary}')
			if isinstance(employee,Manager):
				print(f'Employee Department : {employee.department}')
			if isinstance(employee, Developer):
				print(f'Employee Programming Language : {employee.programming_language}')
			employee.calculate_bonus()
			print('\n')
	else:
		print('No employee to show!')

while True:
	print('Choose an option : ')
	print('1. Add employee')
	print('2. View details of employees')
	choice = int(input('Enter the choice : '))
	
	if choice == 1:
		add_employee()
	elif choice == 2:
		employee_details()
	else:
		print('Invalid Input')
	print('\n')