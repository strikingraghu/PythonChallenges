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


check_amicable_num_validation()