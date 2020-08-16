"""
Problem Link: https://practice.geeksforgeeks.org/problems/add-two-fractions/1
You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and
output the result in the form of (num/den).

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow .
Each test case contains four integers num1, den1, num2, den2 respectively.

Output Format:
For each test case, in a new line,  output will be the fraction in the form a/b where the fraction denotes
the sum of the two given fractions in reduced form.

Your Task:
Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the
function addFraction  which adds the two fractions and prints the resulting fraction.
The function takes four arguments num1, den1, num2, den2 where num1, num2 denotes the numerators
of two fractions and den1, den2 denotes their denominators.

Constraints:
1 <= T <= 100
1 <= den1,den2,num1,num2 <= 1000

Example:
Input
1
1 500 2 500
Output
3/500
Explanation:

In above test case 1/500+2/500=3/500
Note:The Input/Output format and Example given are used for system's internal purpose, and should be
used by a user for Expected Output only. As it is a function problem, hence a user should not read
any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""


def greatest_common_divisor(num_a, num_b):
    if num_b == 0:
        return num_a
    return greatest_common_divisor(num_b, num_a % num_b)


def least_common_multiple(num_a, num_b):
    return (num_a * num_b)//greatest_common_divisor(num_a, num_b)


def add_fractions(num1, denominator1, num2, denominator2):
    den = least_common_multiple(denominator1, denominator2)
    num = num1 * (den//denominator1) + num2 * (den//denominator2)
    gcd_nd = greatest_common_divisor(num, den)
    print(str(num//gcd_nd)+"/"+str(den//gcd_nd))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))
        add_fractions(arr[0], arr[1], arr[2], arr[3])

