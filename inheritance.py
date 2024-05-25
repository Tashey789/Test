class Person:
    def __init__(self, name, age, cid_number):
        # Initialize common attributes for all Person objects
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        # Define behavior for walking
        print(f"{self.name} is walking.")

    def talk(self):
        # Define behavior for talking
        print(f"{self.name} is talking.")

    def eat(self):
        # Define behavior for eating
        print(f"{self.name} is eating.")

    def sleep(self):
        # Define behavior for sleeping
        print(f"{self.name} is sleeping.")


class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year):
        # Initialize Student object with common attributes and additional attributes
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.marks = []  # List to store marks for calculating GPA

    def study(self):
        # Define behavior for studying
        print(f"{self.name} is studying.")

    def attend_class(self):
        # Define behavior for attending class
        print(f"{self.name} is attending class.")

    def write_exam(self):
        # Define behavior for writing an exam
        print(f"{self.name} is writing an exam.")

    def calculate_gpa(self):
        # Method to calculate GPA based on marks
        if not self.marks:  # If marks list is empty, return 0
            return 0
        return sum(self.marks) / len(self.marks)  # Calculate average of marks


class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        # Initialize Teacher object with common attributes and additional attributes
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        # Define behavior for teaching
        print(f"{self.name} is teaching.")

    def grade_students(self):
        # Define behavior for grading students
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        # Define behavior for attending a meeting
        print(f"{self.name} is attending a meeting.")


# Creating objects
student1 = Student("Tashi yangzom", 20, "10601004682", "02230109", "CSF", "first year" )
teacher1 = Teacher("Mrs.Tashi peldon", 90, "106001004678", "CSF", 50000, "ECE", "junior Lecturer")

# Testing behaviors
student1.walk()
student1.talk()
student1.eat()
student1.sleep()
student1.study()
student1.attend_class()
student1.write_exam()

teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()