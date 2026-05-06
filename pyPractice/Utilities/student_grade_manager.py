student_scores = input("Enter student scores separated by comma : ")
scores = [int(score) for score in student_scores.split(",")]

grades = [
	"A" if score >= 90 else
	"B" if score >= 80 else
	"C" if score >= 70 else
	"D" if score >= 60 else
	"F"
	for score in scores
]

passing_students = [score for score in scores if score >= 50]
failing_students = [score for score in scores if score < 50]

print("\n--- Student Scores ---\n", scores)
for i, (score,grade) in enumerate(zip(scores, grades)):
	print(f"Student {i+1}: Score = {score}, Grade = {grade}")

print("\n--- Passing Students ---", passing_students)
print("\n--- Failing Students ---", failing_students)