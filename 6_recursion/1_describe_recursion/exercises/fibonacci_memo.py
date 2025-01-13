#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A recursive implementation of the Fibonacci sequence with memoization.

The Fibonacci sequence is a series of numbers where each number is the
sum of the two preceding ones, starting from 0 and 1.

This function includes:
- Base cases to handle the initial numbers of the sequence.
- Memoization to optimize the recursive solution by storing previously computed results.
"""
import unittest

def fibonacci(n: int, memo: dict = None) -> int:
    """
    Compute the nth Fibonacci number using recursion and memoization.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        memo (dict): A dictionary to store previously computed Fibonacci numbers.

    Returns:
        int: The nth Fibonacci number.

    Base Cases:
        1. If n == 0, return 0 (Fibonacci(0) = 0).
        2. If n == 1, return 1 (Fibonacci(1) = 1).
        3. If n exists in memo, return the stored result (Memoized result).

    Recursive Case:
        - Compute Fibonacci(n-1) and Fibonacci(n-2), then store their sum in memo[n].
    """
    if memo is None:
        memo = {}

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    left_recursion = fibonacci(n - 1, memo)
    right_recursion = fibonacci(n - 2, memo)

    memo[n] = left_recursion + right_recursion
    return memo[n]


# --- --- --- test cases --- --- ---


class TestFibonacci(unittest.TestCase):
    """Unit tests for the fibonacci function."""

    def test_base_case_0(self):
        """Test Fibonacci(0) = 0."""
        self.assertEqual(fibonacci(0), 0)

    def test_base_case_1(self):
        """Test Fibonacci(1) = 1."""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        """Test Fibonacci(2) = 1."""
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_3(self):
        """Test Fibonacci(3) = 2."""
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_4(self):
        """Test Fibonacci(4) = 3."""
        self.assertEqual(fibonacci(4), 3)

    def test_fibonacci_5(self):
        """Test Fibonacci(5) = 5."""
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_6(self):
        """Test Fibonacci(6) = 8."""
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_large(self):
        """Test a larger Fibonacci number."""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_custom_memo(self):
        """Test with a pre-populated memo dictionary."""
        memo = {10: 55, 11: 89}
        self.assertEqual(fibonacci(11, memo), 89)
        self.assertEqual(
            fibonacci(12, memo), 144
        )  # Will compute and store Fibonacci(12) in the memo


if __name__ == "__main__":
    unittest.main()
