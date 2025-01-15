#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script implements the Merge Sort algorithm, a popular divide-and-conquer 
sorting technique. The function takes a list of numbers and returns a sorted list.

Features:
1. Handles edge cases such as an empty list or a single element.
2. Uses recursion to divide the list into smaller parts until base cases are reached.
3. Merges the sorted halves into a single sorted list using a helper function.

Test Cases:
The script includes a few sample test cases to demonstrate the correctness 
of the implementation.
"""

import unittest


def merge_sort(numbers: list) -> list:
    """
    Sorts a list of numbers using the Merge Sort algorithm.

    Args:
        numbers (list): A list of numbers to be sorted.

    Returns:
        list: A sorted list of numbers.

    Process:
    - Base Case: If the list has 0 or 1 element, it's already sorted.
    - Recursive Case: Split the list into two halves, sort each half recursively,
                      and merge the two sorted halves into a single sorted list.
    """
    if len(numbers) <= 1:  # Base case: A list with 0 or 1 element is already sorted.
        return numbers

    mid = len(numbers) // 2  # Find the midpoint of the list.
    
    # Recursive case: Divide and conquer
    left_half = merge_sort(numbers[:mid])  # Sort the left half.
    right_half = merge_sort(numbers[mid:])  # Sort the right half.

    # Merge the sorted halves and return.
    return merge(left_half, right_half)


def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A merged and sorted list containing all elements from 'left' and 'right'.
    """
    sorted_list = []  # Initialize an empty list to hold the sorted elements.
    while left and right:  # Continue until one of the lists is empty.
        if left[0] < right[0]:  # Compare the first elements of both lists.
            sorted_list.append(left.pop(0))  # Append the smaller element to the sorted list.
        else:
            sorted_list.append(right.pop(0))
    
    # Extend the sorted list with any remaining elements from 'left' or 'right'.
    sorted_list.extend(left or right)
    return sorted_list


# Unit test class
class TestMergeSort(unittest.TestCase):
    """Unit tests for the merge_sort function."""

    def test_regular_list(self):
        """Test a regular unsorted list."""
        self.assertEqual(merge_sort([38, 27, 43, 3, 9, 82, 10]), [3, 9, 10, 27, 38, 43, 82])

    def test_sorted_list(self):
        """Test an already sorted list."""
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_order_list(self):
        """Test a list in reverse order."""
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        """Test a list with duplicate elements."""
        self.assertEqual(merge_sort([4, 2, 7, 2, 5, 2]), [2, 2, 2, 4, 5, 7])

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(merge_sort([42]), [42])

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(merge_sort([]), [])

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(merge_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])


# Main block to run the tests
if __name__ == "__main__":
    unittest.main()
