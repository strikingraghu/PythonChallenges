"""
Given an array of integers nums and an integer target, return indices of the two numbers so that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(nums, target):
    fetch_dict = {}
    for i, num in enumerate(nums):
        print(i, num, fetch_dict)
        if target - num in fetch_dict:
            print("$$", [fetch_dict[target - num], i])
        fetch_dict[num] = i


two_sum([0, 1, 4, 8], 9)
