"""
This is a Python Program to read height in centimeters and then convert the height to feet and inches

Problem Description
The program reads the height in centimeters and then converts the height to feet and inches.

Problem Solution
1. Take the height in centimeters and store it in a variable.
2. Convert the height in centimeters into inches and feet.
3. Print the length in inches and feet.
4. Exit.
"""


def calculate_height_value():
    print()
    height_centimeters = int(input("Enter the height of a person to get it convereted to feet & inches value: "))
    height_feet_value = 0.0328 * height_centimeters
    height_inches_value = 0.394 * height_centimeters
    print("Value after conversion is", round(height_feet_value, 2), "feet or", round(height_inches_value, 2), "inches")


calculate_height_value()
