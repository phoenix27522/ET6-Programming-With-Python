#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""demo implementing recursive strategies"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def reverse_list(to_reverse: list) -> list:
    # Base case: If the list has 0 or 1 element, it's already reversed
    base_case = len(to_reverse) <= 1
    if base_case:
        turn_around = to_reverse
        return turn_around

    # Recursive case: Break down the problem
    break_down = to_reverse[1:]  # Remove the first element
    recursion = reverse_list(break_down)  # Recursively reverse the rest
    build_up = recursion + [to_reverse[0]]  # Append the first element at the end

    return build_up


# ----- ----- test cases ----- -----

print(reverse_list([]), 'should be', [])
print(reverse_list([1, 2]), 'should be', [2, 1])
print(reverse_list([1, 2, 3]), 'should be', [3, 2, 1])
print(reverse_list([3, 2, 1, 0, -1, -2, 3]), 'should be', [3, -2, -1, 0, 1, 2, 3])
