""" Common module
implement commonly used functions here
"""

import random


def get_random_char_between(letter_1, letter_2):
    return chr(random.randint(ord(letter_1), ord(letter_2)))


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

    keys = [row[0] for row in table]

    generated_in_keys = True
    while generated_in_keys:
        generated = ''
        for _ in range(2):
            generated += get_random_char_between("a", "z")
            generated += get_random_char_between("A", "Z")
            generated += get_random_char_between("!", "/")
            generated += get_random_char_between("0", "9")

        if not (generated in keys):
            generated_in_keys = False

    return generated
