"""
This is a Python Program to check if a date is valid and print the incremented date if it is.

Problem Description
The program takes in a date and checks if it a valid date and prints the incremented date if it is.

Problem Solution
1. Take in the date of the form: dd/mm/yyyy.
2. Split the date and store the day, month and year in separate variables.
3. Use various if-statements to check if the day, month and year are valid.
4. Increment the date if the date is valid and print it
5. Exit.
"""


def validate_date():
    print()
    user_input = input("Enter a date of your choice in dd/mm/yyyy format: ").split("/")
    date_value = int(user_input[0])
    month_value = int(user_input[1])
    year_value = int(user_input[2])

    # validations towards date's value
    if date_value == 00:
        print("Provided date in the user input is not a valid one!")
    elif month_value == 2 and date_value > 29:
        print("Provided date value is not a valid one!")
    else:
        print("Thanks, date provide is valid")

    # validations towards month's value
    if month_value == 00 or month_value > 13:
        print("Provided month in the user input is not a valid one!")
    else:
        print("Thanks, month provide is valid")

    # validations towards month's value
    leap_year = False
    if year_value % 4 == 0 and year_value % 100 != 0 and year_value % 400 == 0:
        leap_year = True
        print("Thanks for providing a leap year!")

    # date value increments
    increased_date_value = 0
    increased_month_value = 0
    increased_year_value = 0

    if date_value == 28 and month_value == 2 and leap_year != False:
        increased_date_value = increased_date_value + 29
    elif date_value == 31 and month_value > 0:
        increased_date_value = increased_date_value + 1
    else:
        increased_date_value = date_value + 1

    # month value increments
    if date_value == 31 and month_value == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        increased_month_value = increased_month_value + month_value + 1
    elif date_value == 30 and month_value == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        increased_month_value = increased_month_value + month_value
    elif date_value == 30 and month_value == 4 or 6 or 9 or 11:
        increased_month_value = increased_month_value + month_value + 1
    elif date_value > 0 < 28 and month_value != 2 <= 12:
        increased_month_value = increased_month_value + month_value

    # year value increments
    if date_value == 31 and month_value == 12:
        increased_year_value = increased_year_value + year_value + 1
    else:
        increased_year_value = year_value

    print("Next date would be: ", increased_date_value, "/", increased_month_value, "/", increased_year_value)


validate_date()
