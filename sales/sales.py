""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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

    title_list = ['ID', 'Title', 'Price', 'Month', 'Day', 'Year', 'Customer ID']
    common.show_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ['Title:', 'Price:', 'Month:', 'Day:', 'Year:', 'Customer ID:']
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

    title_list = ['Title', 'Price', 'Month', 'Day', 'Year', 'Customer ID']
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
    # your code


# functions supports data abalyser
# --------------------------------

def get_column_index(column_name):
    columns = ("id", "title", "price", "month", "day", "year", "customer_id")
    for index, column in enumerate(columns):
        if column == column_name:
            return index


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    table = data_manager.get_table_from_file
    id = ui.get_inputs
    for id in table:
        if table[0] == id:
            return table[1]
            


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    file_name = 'sales/sales.csv'
    table = data_manager.get_table_from_file(file_name)

    return get_item_id_sold_last_from_table(table)


def get_sale_date(sale_record):
    year = int(sale_record[get_column_index("year")])
    month = int(sale_record[get_column_index("month")])
    day = int(sale_record[get_column_index("day")])

    return (year, month, day)


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    last_sale_record = max(table, key=get_sale_date)
    return last_sale_record[get_column_index("id")]


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    table = data_manager.get_table_from_file('sales/sales.csv')
    return get_the_sum_of_prices_from_table(table, item_ids) 


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    sum_of_prices = 0
    price_index = 2
    id_index = 0
    for record in table:
        if record[id_index] in item_ids:
            sum_of_prices += int(record[price_index])
    return sum_of_prices


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    return get_customer_id_by_sale_id_from_table(table, sale_id)


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    customer_id_index = 6
    sale_id_index = 0
    for record in table:
        if record[sale_id_index] == sale_id:
            return record[customer_id_index]


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    return get_all_customer_ids_from_table(table)


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """
    all_customer_ids = set()
    for record in table:
        all_customer_ids.add(record[get_column_index('customer_id')])
    return all_customer_ids


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
