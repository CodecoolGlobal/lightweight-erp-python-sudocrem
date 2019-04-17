""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

    menu = ['Display table', 'Add', 'Remove', 'Update', 'Get lowest priced items ID', 'Filter between dates']
    file_name = 'sales/sales.csv'
    table = data_manager.get_table_from_file(file_name)
    while True:
        ui.print_menu(
            'Sales',
            menu,
            'Go back to main menu')
        sales_input = ui.get_inputs(["Please enter a number:"], "")
        if sales_input[0] == '0':
            return None
        elif sales_input[0] == '1':
            show_table(table)
        elif sales_input[0] == '2':
            table = add(table)
        elif sales_input[0] == '3':
            table = remove(table, ui.get_inputs(['ID'], "Removing")[0])
        elif sales_input[0] == '4':
            table = update(table, ui.get_inputs(['ID'], "Updating")[0])
        elif sales_input[0] == '5':
            ui.print_result(get_lowest_price_item_id(table), 'Get lowest priced items ID')
        elif sales_input[0] == '6':
            year_from, month_from, day_from, year_to, month_to, day_to = ui.get_inputs(['Year from:', 'Month from:', 'Day from:','Year to:','Month to:', 'Day to:'], "Filters")
            ui.print_result(get_items_sold_between(table, int(month_from), int(day_from), int(year_from), int(month_to), int(day_to), int(year_to)), 'Records between specified dates')

        data_manager.write_table_to_file(file_name, table)

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'Title', 'Price', 'Month', 'Day', 'Year']
    common.show_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ['Title:', 'Price:', 'Month:', 'Day:', 'Year:']
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

    title_list = ['Title', 'Price', 'Month', 'Day', 'Year']
    return common.update(table, id_, title_list)


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    price_index = 2
    ID_index = 0
    lowest_price_item_id = min(table, key = lambda x: x[price_index])[ID_index]
    return lowest_price_item_id



def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    month_index = 3
    day_index = 4
    year_index = 5

    filtered_records = []
    for record in table:
        if year_from <= int(record[year_index]) <= year_to:
            if (int(record[year_index]) == year_from) or (int(record[year_index]) == year_to):
                if month_from <= int(record[month_index]) <= month_to:
                    if (int(record[month_index]) == month_from) or (int(record[month_index]) == month_to):
                        if day_from <= int(record[day_index]) <= day_to:
                            if (int(record[day_index]) == day_from) or (int(record[day_index]) == day_to):
                                pass
                            else:
                                filtered_records.append(record)
                    else:
                        filtered_records.append(record)
            else:
                filtered_records.append(record)
    
    for filtered_record in filtered_records:
        for index in range(2,6):
            filtered_record[index] = int(filtered_record[index])
     
    return filtered_records
