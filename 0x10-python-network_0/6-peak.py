#!/usr/bin/python3
"""function to find peak"""


def find_peak(list_of_integers):
    """function to find peak in a list of integers"""
    lenoflist = len(list_of_integers)
    nums = list_of_integers
    for i in range(lenoflist):
        if (nums[i] >= nums[i - 1]) and (nums[i] >= nums[i + 1]):
            return nums[i]

