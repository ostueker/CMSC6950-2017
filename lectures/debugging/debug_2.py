#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 2 for using the interactive debugger.

This program imports a bad "means" function that
will run in an infinite loop!
"""
import debug_mean

if __name__ == "__main__":

    a_list = [1, 2, 3, 4, 5, 6, 10, "one hundred"]
    debug_mean.mean(a_list)
