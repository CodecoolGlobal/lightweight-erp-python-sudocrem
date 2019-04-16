""" Common module
implement commonly used functions here
"""

import random
import ui


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

    shuffled = ''.join(random.sample(generated, len(generated)))
    return shuffled


def show_table(table, title_list):
    ui.print_table(table, title_list)


def add(table, title_list):
    new_record = []
    new_record.append(generate_random(table))
    new_record.extend(ui.get_inputs(title_list, 'Enter new record'))
    table.append(new_record)
    return table


def remove(table, id_):
    for element in table:
        if element[0] == id_:
            table.remove(element)
    return table


def update(table, id_, title_list):
    return_element = []
    for element in table:
        if element[0] == id_:
            return_element.append(element[0])
            return_element.extend(ui.get_inputs(title_list, 'Update record'))
            for index, data in enumerate(return_element):
                if not data:
                    data = element[index]
            table.remove(element)
            break
    table.append(return_element)
    return table