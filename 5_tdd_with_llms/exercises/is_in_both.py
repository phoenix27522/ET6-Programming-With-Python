""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

"""
def is_in_both(item, list1, list2):
    """
    Checks if the given item is present in both lists.

    Args:
        item (str): The string to check.
        list1 (list of str): The first list of strings.
        list2 (list of str): The second list of strings.

    Returns:
        bool: True if the item is in both lists, False otherwise.
    """
    return item in list1 and item in list2
