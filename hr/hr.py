""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

TITLES = ['Name', 'Birth year']
NAME, BIRTH = (1, 2)


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    menu = ['Display table', 'Add', 'Remove', 'Update']
    file_name = 'hr/persons.csv'

    while True:
        table = data_manager.get_table_from_file(file_name)

        ui.print_menu(
            'Human resources manager',
            menu,
            'Go back to main menu')
        crm_input = ui.get_inputs(["Please enter a number:"], "")
        if crm_input[0] == '0':
            return None
        elif crm_input[0] == '1':
            show_table(table)
        elif crm_input[0] == '2':
            table = add(table)
        elif crm_input[0] == '3':
            table = remove(table, ui.get_inputs(['ID'], "Removing")[0])
        elif crm_input[0] == '4':
            table = update(table, ui.get_inputs(['ID'], "Updating")[0])

        data_manager.write_table_to_file(file_name, table)


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID"] + TITLES
    common.show_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    return common.add(table, TITLES)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    return common.remove(table, id_)


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    return common.update(table, id_, TITLES)


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    min_birth_year = min(int(person[BIRTH]) for person in table)
    return [person[NAME] for person in table if int(person[BIRTH]) == min_birth_year]


def average(numbers):
    length = len(numbers)
    if length == 0:
        return 0

    sum_ = 0
    for number in numbers:
        sum_ += number
    return sum_ / length


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # equivalent to: who's birth year is closest to the average birth year?
    birth_years = [int(person[BIRTH]) for person in table]
    average_year = average(birth_years)

    min_dist = min(abs(average_year - int(person[BIRTH])) for person in table)
    closest_persons_names = []
    for person in table:
        if abs(average_year - int(person[BIRTH])) == min_dist:
            closest_persons_names.append(person[NAME])
    return closest_persons_names
