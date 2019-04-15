""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # your code

    return generated


def get_longest_elements(table):
    """
    Returns a list of integers, containing the length of the longest element in a column.
    Looks awful, but works...
    """
    columns = len(table[0])
    longest_elements = [0] * columns
    for column in range(columns):
        max_column_length = 0
        for line in table:
            column_element = line[column]
            if len(column_element) > max_column_length:
                max_column_length = len(column_element)
        longest_elements[column] = max_column_length
    return longest_elements




