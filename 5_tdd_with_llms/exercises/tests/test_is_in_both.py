"""
Module to test the is_in_both function, which checks if an item is present in both lists.
The tests cover various scenarios including items in both lists, one list, or neither.
"""

import unittest
from is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """
    Test class for the is_in_both function. It includes tests for the following scenarios:
    - Item is present in both lists
    - Item is not in both lists
    - Item is in only one list
    - Item is not in any list
    - One or both lists are empty
    - Case sensitivity of the function
    """

    def test_item_in_both_lists(self):
        """
        Test if the function returns True when the item is in both lists.
        """
        self.assertTrue(is_in_both("apple", ["apple", "banana"], ["apple", "cherry"]))
        self.assertTrue(is_in_both("cherry", ["cherry", "date"], ["cherry", "banana"]))

    def test_item_not_in_both_lists(self):
        """
        Test if the function returns False when the item is not in both lists.
        """
        self.assertFalse(is_in_both("banana", ["apple", "banana"], ["cherry", "date"]))
        self.assertFalse(is_in_both("date", ["apple", "cherry"], ["cherry", "banana"]))

    def test_item_in_one_list_only(self):
        """
        Test if the function returns False when the item is in only one list.
        """
        self.assertFalse(is_in_both("apple", ["apple", "banana"], ["cherry", "date"]))
        self.assertFalse(is_in_both("date", ["cherry", "date"], ["apple", "banana"]))

    def test_item_not_in_any_list(self):
        """
        Test if the function returns False when the item is not in either list.
        """
        self.assertFalse(is_in_both("kiwi", ["apple", "banana"], ["cherry", "date"]))

    def test_empty_lists(self):
        """
        Test if the function returns False when one or both lists are empty.
        """
        self.assertFalse(is_in_both("apple", [], []))
        self.assertFalse(is_in_both("apple", ["apple"], []))
        self.assertFalse(is_in_both("apple", [], ["apple"]))

    def test_case_sensitivity(self):
        """
        Test if the function is case-sensitive, distinguishing between 'Apple' and 'apple'.
        """
        self.assertFalse(is_in_both("Apple", ["apple", "banana"], ["apple", "cherry"]))
        self.assertTrue(is_in_both("apple", ["apple", "banana"], ["apple", "cherry"]))


if __name__ == "__main__":
    unittest.main()
