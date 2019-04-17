""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
    # you code
    file_name = 'accounting/items.csv'
    table = data_manager.get_table_from_file("accounting/items.csv")
    accounting_options = [
        "Show table",
        "Add to table",
        "Remove from table",
        "Update table",
        "Year of highest profit",
        "Annual average"]
    while True:
        ui.print_menu("Accounting menu:", accounting_options, "Go back to main menu:")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            get_id = ui.get_inputs(["Please enter an ID to remove: "], "")
            id_ = get_id[0]
            remove(table, id_)
        elif option == "4":
            get_id = ui.get_inputs(["Please enter an ID to update: "], "")
            id_ = get_id[0]
            update(table, id_)
        elif option == "5":
            year_max = which_year_max(table)
            ui.print_result(year_max, "Year of highest profit")
        elif option == "6":
            year = int(ui.get_inputs(["Please give a year: "], "")[0])
            avg_year = avg_amount(table, year)
            ui.print_result(avg_year, "Annual profit average")
        elif option == "0":
            return None
        else:
            raise KeyError("There is no such option.")
        data_manager.write_table_to_file(file_name, table)


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # your code
    title_list = ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount']
    common.show_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    # your code
    title_list = ['Month', 'Day', 'Year', 'Type', 'Amount']
    return common.add(table, title_list)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
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

    # your code
    title_list = ['Month', 'Day', 'Year', 'Type', 'Amount']
    return common.update(table, id_, title_list)


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)
    Args:
        table (list): data table to work on
    Returns:
        number
    """
    # your code
    # type (string): in = income, out = outflow

    data_year = 3
    data_type = 4
    data_amount = 5
    profit_max = 0
    year_max = 0
    actual_year = 0
    profit = 0

    for data in table:
        actual_year = data[data_year]
        if data[data_year] == actual_year:
            if data[data_type] == "in":
                profit += int(data[data_amount])
            elif data[data_type] == "out":
                profit -= int(data[data_amount])
        if profit > profit_max:
            year_max = int(actual_year)
            profit_max = profit
        
    return year_max


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]
    Args:
        table (list): data table to work on
        year (number)
    Returns:
        number
    """
    # your code

    data_year = 3
    data_type = 4
    data_amount = 5
    profit_of_year = 0
    items_count = 0

    for data in table:
        if int(data[data_year]) == year:
            if data[data_type] == "in":
                profit_of_year += int(data[data_amount])
                items_count += 1
            elif data[data_type] == "out":
                profit_of_year -= int(data[data_amount])
                items_count += 1
    avg_amount = (profit_of_year / items_count)
    return avg_amount
