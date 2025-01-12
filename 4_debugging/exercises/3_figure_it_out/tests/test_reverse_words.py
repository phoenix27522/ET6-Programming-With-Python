#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for reverse_words function.
Contains correct tests to help identify bugs in the implementation.
    careful! these tests may have bugs too.

Test categories:
    - Standard cases: typical string lists
    - Edge cases: empty strings, equal lengths
    - Defensive tests: invalid inputs

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from reverse_words import reverse_words


class TestReverseWords(unittest.TestCase):
    """Test the reverse_words function"""

    def test_empty_string(self):
        """It should return empty string for empty input"""
        self.assertEqual(reverse_words(""), "")  # probably ok

    def test_one_word(self):
        """It should return the same string for one word"""
        self.assertEqual(reverse_words("hello"), "hello")  # probably ok

    def test_two_words(self):
        """It should reverse two words"""
        self.assertEqual(reverse_words("hello world"), "world hello")  # probably ok

    def test_two_spaces(self):
        """It should handle two spaces"""
        self.assertEqual(reverse_words("hello  world"), "world hello")  # probably ok

    def test_three_spaces(self):
        """It should handle three spaces"""
        self.assertEqual(reverse_words("hello   world"), "world hello")  # probably ok

    def test_only_spaces(self):
        """It should return an empty string for input with only spaces"""
        self.assertEqual(reverse_words("     "), "")

    def test_multiple_words(self):
        """It should reverse multiple words"""
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")
        self.assertEqual(reverse_words(" a b c d "), "d c b a")

    def test_numeric_string(self):
        """It should reverse words in a numeric string"""
        self.assertEqual(reverse_words("123 456 789"), "789 456 123")

    def test_special_characters(self):
        """It should reverse words with special characters"""
        self.assertEqual(reverse_words("hello! world?"), "world? hello!")
        self.assertEqual(reverse_words("one@ two# three$"), "three$ two# one@")

    def test_invalid_input(self):
        """It should raise an assertion error for invalid input types"""
        with self.assertRaises(AssertionError):
            reverse_words(123)  # Input is not a string
        with self.assertRaises(AssertionError):
            reverse_words(None)  # Input is not a string
