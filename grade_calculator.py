# # print("Hello world!")

# # Practice Problem 2: Student Grade Calculator
# #==============================================#

# Create a Python program named grade_calculator.py that:
# 1. Takes a student's name as input.
# 2. Takes avg for three subjects.
# 3. Calculates the Average avg.
# # 4. Determines the grade using the following conditions:

stuname = input("Enter student name: ")

sub1 = float(input("\nEnter Math marks: "))
sub2 = float(input("Enter English marks: "))
sub3 = float(input("Enter Python marks: "))

# Calculate average
avg = round((sub1 + sub2 + sub3) / 3, 2)

# Validate marks
if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
    print("\n\nInvalid marks")

# Calculate grade and output
else:
    if avg >= 80 and avg <= 100:
        print(f" \n\nStudent Name: {stuname} \nAverage marks: {avg} \nGrade: A+")

    elif avg >= 70 and avg <= 79:
        print(f" \n\nStudent Name: {stuname} \nAverage marks: {avg} \nGrade: A")

    elif avg >= 60 and avg <= 69:
        print(f" \n\nStudent Name: {stuname} \nAverage marks: {avg} \nGrade: A-")

    elif avg >= 50 and avg <= 59:
        print(f" \n\nStudent Name: {stuname} \nAverage marks: {avg} \nGrade: B")

    elif avg >= 40 and avg <= 49:
        print(f" \n\nStudent Name: {stuname} \nAverage marks: {avg} \nGrade: C")

    else:
        print(f" \n\nStudent Name: {stuname} \nAverage marks: {avg} \nGrade: F")


