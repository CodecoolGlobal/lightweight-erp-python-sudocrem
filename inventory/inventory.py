""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

TITLES = ['Name', 'Manufacturer', "Purchase year", "Durability"]
NAME, MANUFACTURER, PURCHASE_YEAR, DURABILITY = tuple(range(1, len(TITLES)+1))


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    menu = ['Display table', 'Add', 'Remove', 'Update', 'Oldest person', 'Closest to average age']
    file_name = 'hr/persons.csv'

    while True:
        table = data_manager.get_table_from_file(file_name)

        ui.print_menu(
            'Inventory manager',
            menu,
            'Go back to main menu')
        inventory_input = ui.get_inputs(["Please enter a number:"], "")
        if inventory_input[0] == '0':
            return None
        elif inventory_input[0] == '1':
            show_table(table)
        elif inventory_input[0] == '2':
            table = add(table)
        elif inventory_input[0] == '3':
            table = remove(table, ui.get_inputs(['ID'], "Removing")[0])
        elif inventory_input[0] == '4':
            table = update(table, ui.get_inputs(['ID'], "Updating")[0])
        elif inventory_input[0] == '5':
            ui.print_result(get_available_items(table), "Available items")
        elif inventory_input[0] == '6':
            ui.print_result(get_average_durability_by_manufacturers(table), "Average durability by manufacturers")
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

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    current_date = 2016
    available_items = []

    for element in table:
        if (int(element[PURCHASE_YEAR]) + int(element[DURABILITY])) > current_date:
            available_items.append(element)
    for available_item in available_items:
        for index in range(3,5):
            available_item[index] = int(available_item[index])
    return available_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    manufacturers = set(product[MANUFACTURER] for product in table)

    avg_durs = {}
    for manufacturer in manufacturers:
        durabilities_for_manuf = []
        for product in table:
            if product[MANUFACTURER] == manufacturer:
                durabilities_for_manuf.append(int(product[DURABILITY]))
                
        avg_durs[manufacturer] = common.average(durabilities_for_manuf)

    return avg_durs
