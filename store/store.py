""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = data_manager.get_table_from_file('store/games.csv')
    options = ["Display table",
               "Add to table",
               "Remove",
               "Update table",
               "Count by manufactureres",
               "Average by manufacturer"]

    while True:
        ui.print_menu("Store manager", options, "Go back to main")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            common.remove(table, ui.get_inputs(['ID'], '')[0])
            data_manager.write_table_to_file('store/games.csv', table)
        elif option == "4":
            title_list = ['Name', 'Manufacturer', 'Price', 'In stock']
            common.update(table, ui.get_inputs(['ID'], '')[0], title_list)
            data_manager.write_table_to_file('store/games.csv', table)
        elif option == "0":
            return None
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['ID', 'Name', 'Manufacturer', 'Price', 'In stock']
    common.show_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_list = ['Name', 'Manufacturer', 'Price', 'In stock']
    common.add(table, title_list)
    return table


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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    common.update(table, id_, title_list)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    return_dict = {}
    for game in table:
        if game[2] in return_dict:
            return_dict[game[2]] += 1
        else:
            return_dict.update({game[2]:1})
    return return_dict
    


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    title_count = 0
    stock_count = 0
    for record in table:
        if record[2] == manufacturer:
            stock_count += int(record[4])
            title_count += 1
    return stock_count / title_count


