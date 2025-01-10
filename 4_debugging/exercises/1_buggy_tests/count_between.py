#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting numbers within a range.
This is part of the debugging exercise series focusing on buggy tests.

Module contents:
    - count_between: Counts how many numbers fall between two values

Created on 2024-12-06
Author: Claude AI
"""


def count_between(numbers: list, lower: float, upper: float) -> int:
    """Counts how many numbers in the list fall between lower and upper bounds.

    The bounds are inclusive, meaning a number equal to the lower or upper
    bound is counted. The numbers list can contain integers or floats.

    Parameters:
        numbers: list of numbers to check
        lower: float, lower bound (inclusive)
        upper: float, upper bound (inclusive)

    Returns -> int: count of numbers between bounds

    Raises:
        AssertionError: if numbers is not a list or bounds aren't integers/floats

    Examples:
        >>> count_between([1, 2, 3, 4, 5], 2, 4)
        3
        >>> count_between([1.5, 2.5, 3.5], 2, 3)
        1
        >>> count_between([], 0, 10)
        0
    """
    assert isinstance(numbers, list), "first argument must be a list"
    assert isinstance(lower, (int, float)), (
        "lower bound must be a number (int or float)"
    )
    assert isinstance(upper, (int, float)), (
        "upper bound must be a number (int or float)"
    )

    # Ensure bounds are in the correct order
    if lower > upper:
        lower, upper = upper, lower

    # Count numbers within the inclusive range
    return sum(lower <= num <= upper for num in numbers)
