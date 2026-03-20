import csv
import os

current_dir = os.path.dirname(__file__)   
base_dir = os.path.dirname(current_dir)  
file_path = os.path.join(base_dir, 'datasets', 'student_data.csv')

def process_student_data(input_file, output_file):
	try:
		with open(input_file, 'r') as infile:
			reader = csv.DictReader(infile)
			student_reports = []

			for row in reader:
				name = row['Name']
				math = int(row['Math'])
				science = int(row['Science'])
				english = int(row['English'])
				average = round((math + science + english)/3 , 2)
				status = "Pass" if average >= 60 else "Fail"

				student_reports.append({
					'Name': name,
					'Math': math,
					'Science': science,
					'English': english,
					'Average': average,
					'Status': status
				})

		with open(output_file, 'w', newline='') as outfile:
			fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
			writer = csv.DictWriter(outfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(student_reports)

		print(f"Report generated successfully in {output_file}")

	except Exception as e:
		print(f"An error occurred: {e}")

input_file = file_path
output_file = os.path.join(base_dir, 'datasets', 'student_report.csv')

process_student_data(input_file, output_file)