""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    menu = ['Display table', 'Add', 'Remove', 'Update']
    table = data_manager.get_table_from_file('crm/customers.csv')
    while True:
        ui.print_menu(
            'Customer Relationship Management (CRM)',
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


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    table.remove(element)Returns:
        None
    """
    title_list = ['ID', 'Name', 'Email', 'Subscribed']
    common.show_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_list = ['Name:', 'Email:', 'Subscribed:']
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

    title_list = ['Name', 'Email', 'Subscribed']
    return common.update(table, id_, title_list)


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name,
# separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
