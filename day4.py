#Program: Student Marks and Percentage

student_name = input("Enter student name:")
subject1 = int(input("Enter marks in subject1: "))
subject2 = int(input("Enter marks in subject2: "))
subject3 = int(input("Enter marks in subject3: "))

total = subject1 + subject2 + subject3
percentage = total/3

print("\n----------Student Report-----------")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Percentage:", percentage)