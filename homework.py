# Ask the user to input their age
age = int(input("Enter your age: "))

# Ask the user to input whether they are a student or not
is_student = input("Are you a student? (yes/no): ")

#use logical operator to determine eligibility for discount
if age <= 13 or (age >= 15 and age <= 18 and is_student == "yes"):
    print("you are eligible for a discount on the movie ticket!")
else:
    print("you are not eligible for a discount on the movie ticket")    
    