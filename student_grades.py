num_students = int(input("Enter the number of students: "))

i = 1
while i <= num_students:
    total_grade = 0
    num_students = int(input("Enter the number of subjects for students {i}: "))

for j in range(1, num_students + 1):
    grade = float(input(f"Enter subject {j} grade for students {i}: "))
    total_grade += grade

average_grade = total_grade / num_students
print(f"average grade for students {i}: {average_grade:.2f}")
i += 1


