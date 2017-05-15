#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 1 for using the interactive debugger.

This program ends up in an infinite loop!
"""

def mean(nums):
    bot = len(nums)
    it = 0
    top = 0
    while it < len(nums):
        top += nums[it]
    return float(top) / float(bot)

if __name__ == "__main__":
    a_list = [1, 2, 3, 4, 5, 6, 10, "one hundred"]
    mean(a_list)
