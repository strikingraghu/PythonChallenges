# When input() function executes program flow will be stopped until the user has given an input.
# The text or message display on the output screen to ask a user to enter input value is optional.
# Which means, the prompt, will be printed on the screen is optional.
# Whatever you enter as input, input function convert it into a string.
# If you enter an integer value still input() function convert it into a string.
# You need to explicitly convert it into an integer in your code using typecasting.

num = input("Enter the number of your choice: ")
print("Number provided by you is: ", num)

name = input("Enter any name of your choice: ")
print("Name that's been entered is: ", name)

# Typecasting Functions


def typecasting():

    given_value = input("Enter the number of your choice: ")
    for element in given_value:
        typecasting_value = int(element)
        try:
            if type(typecasting_value) == int:
                print("Thanks, entered value is an integer")
        except ValueError as e:
            if type(typecasting_value) != int:
                print("Err, please enter a valid integer!")
            print(e.__class__)


typecasting()

