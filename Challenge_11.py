"""
This is a Python Program to reverse a given number.

Problem Description
The program takes a number and reverses it.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and store the reversed number in another variable.
3. Print the reverse of the number.
4. Exit.
"""


def reverse_number_value():
    print()

    incoming_values = int(input("Enter any number: "))
    reversed_value = 0
    while incoming_values > 0:
        digit = incoming_values % 10
        print("digit =", digit)
        reversed_value = reversed_value * 10 + digit
        print("reversed_value =", reversed_value)
        incoming_values = incoming_values // 10
        print("incoming_values =", incoming_values)
    print("Final value of reversing a provided number =", reversed_value)


# calling function
reverse_number_value()


"""
This is a Python Program to take in the marks of 5 subjects and display the grade.

Problem Description
The program takes in the marks of 5 subjects and displays the grade.

Problem Solution
1. Take in the marks of 5 subjects from the user and store it in different variables.
2. Find the average of the marks.
3. Use an else condition to decide the grade based on the average of the marks.
4. Exit.
"""


def finding_student_grades():
    print()

    marks = [int(x) for x in input("Enter your marks by providing space between each subject: ").split()]
    total_marks = 0
    for each_subject_marks in marks:
        total_marks = total_marks + each_subject_marks
    subjects_applicable = len(marks)
    average_score = total_marks / subjects_applicable
    print("Your average score :", average_score)

    if average_score > 85.0:
        print("Congrats, you have scored distinction!")
    elif average_score > 60.0 and average_score <= 85.0:
        print("Nice, you have scored first class marks")
    elif average_score > 50.0 and average_score <= 60.0:
        print("Good, you have scored second class marks")
    elif average_score >= 35.0 and average_score <= 50.0:
        print("Good, you have scored third class marks")
    else:
        print("Sorry, you have failed in one of subject. Hard luck!")


# calling function
finding_student_grades()
