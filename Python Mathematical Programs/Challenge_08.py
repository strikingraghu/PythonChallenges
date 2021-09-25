"""
Problem Description
The program takes two numbers and checks if they are amicable numbers.

Problem Solution
1. Take in both the integers and store it in separate variables.
2. Find the sum of the proper divisors of both the numbers.
3. Check if the sum of the proper divisors is equal to the opposite numbers.
4. If they are equal, they are amicable numbers.
5. Print the final result.
6. Exit.
"""

import math


def check_amicable_num_validation():


    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        if type(x or y) == int:
            print("Provided input values are part of integer category")

            sum1 = 0
            sum2 = 0
            for i in range(1,x):
                if x % i == 0:
                    print(i)
                    sum1 += i
            print("Closing execution for x value")

            for j in range(1,y):
                if y % j == 0:
                    print(j)
                    sum2 += j
            print("Closing the execution for y value")

            if sum1 == y and sum2 == x:
                print("Above provided numbers are amicable")
            else:
                print("Above provided numbers are not amicable!")
                
    except (BaseException, UnboundLocalError, ValueError) as e:
        print("Logging error: ", e)
        print("Please check the provided input values!")


# check_amicable_num_validation()


"""
Problem Description
The program takes three sides of a triangle and prints the area formed by all three sides.

Problem Solution
1. Take in all the three sides of the triangle and store it in three separate variables.
2. Then using the Heron’s formula, compute the area of the triangle.
3. Print the area of the triangle.
4. Exit.
"""


def calculate_triangle_area():
    
    try:
        x = int(input("Enter the value of first side: "))
        y = int(input("Enter the value of second side: "))
        z = int(input("Enter the value of third side: "))

        if type(x and y and z) == int:
            area = (x + y + z) / 2
            print("Getting into the calculation!")
            triange_area = math.sqrt(area * (area-x)*(area-y)*(area-z))
            
        print("Area of Triangle is around = ", round(triange_area, 2))
    except (KeyboardInterrupt, ValueError, UnboundLocalError) as e:
        print("Logging error: ", e)
        print("Please check the provided input values!")


# calculate_triangle_area()


"""
Problem Description
The program takes in a number and checks if it is a prime number.

Problem Solution
1. Take in the number to be checked and store it in a variable.
2. Initialize the count variable to 0.
3. Let the for loop range from 2 to half of the number (excluding 1 and the number itself).
4. Then find the number of divisors using the if statement and increment the count variable each time.
5. If the number of divisors is lesser than or equal to 0, the number is prime.
6. Print the final result.
5. Exit.
"""


def check_prime_number():

    incoming_val = int(input("Enter the number: "))
    counter_value = 0

    for i in range(2, incoming_val//2+1):
        if (incoming_val % i == 0):
            counter_value = counter_value + 1
    if counter_value <= 0:
        print("Provided number is prime")
    else:
        print("Provide number is not prime!")

check_prime_number()
