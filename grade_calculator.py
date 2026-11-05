# # print("Hello world!")

# # Practice Problem 2: Student Grade Calculator
# #==============================================#

# Create a Python program named grade_calculator.py that:
# 1. Takes a student's name as input.
# 2. Takes avg for three subjects.
# 3. Calculates the Average avg.
# # 4. Determines the grade using the following conditions:

stuname = input("student name: ")
sub1 = int(input("subject1 : "))
sub2 = int(input("subject2 : "))
sub3 = int(input("subject3 : "))

avg = int((sub1 + sub2 + sub3) / 3)
print(avg)

if avg >= 80 and avg <= 100:
    print(f" Student Name: {stuname} \n Average marks: {avg} \n Grade: A+")

elif avg >= 70 and avg <= 79:
    print(f" Student Name: {stuname} \n Average marks: {avg} \n Grade: A")

elif avg >= 60 and avg <= 69:
    print(f" Student Name: {stuname} \n Average marks: {avg} \n Grade: A-")

elif avg >= 50 and avg <= 59:
    print(f" Student Name: {stuname} \n Average marks: {avg} \n Grade: B")

elif avg >= 40 and avg <= 49:
    print(f" Student Name: {stuname} \n Average marks: {avg} \n Grade: C")

elif avg < 40:
    print(f" Student Name: {stuname} \n Average marks: {avg} \n Grade: F")


else:
    print("invalid marks")

