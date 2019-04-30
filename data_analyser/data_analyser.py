"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        get_the_last_buyer_name()
    elif option == "2":
        get_the_last_buyer_id()
    elif option == "3":
        get_the_buyer_name_spent_most_and_the_money_spent()
    elif option == "4":
        get_the_buyer_id_spent_most_and_the_money_spent()
    elif option == "5":
        get_the_most_frequent_buyers_names()
    elif option == "6":
        get_the_most_frequent_buyers_ids()
    elif option == "0":
        return None
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Data analyzer"]

    ui.print_menu("Main menu", options, "Exit program")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    handle_menu()
    go_to_menu = choose
    return go_to_menu


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    item_id = sales.get_item_id_sold_last()
    customer_name = crm.get_name_by_id(item_id)
    return customer_name


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """
    sale_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(sale_id)
    return customer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    most_spent_customer_id_moneys = get_the_buyer_id_spent_most_and_the_money_spent()
    customer_id = most_spent_customer_id_moneys[0]
    customer_name = crm.get_name_by_id(customer_id)
    most_spent_name_moneys = (customer_name, most_spent_customer_id_moneys[1])
    return most_spent_name_moneys


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    all_sales_ids_for_customer_ids = sales.get_all_sales_ids_for_customer_ids()
    most_money_spent = 0

    for customer_id, sale_ids in all_sales_ids_for_customer_ids:
        money_spent_per_buyer = sales.get_the_sum_of_prices(sale_ids)
        if money_spent_per_buyer > most_money_spent:
            customer_id_spent_most = customer_id
            most_money_spent = money_spent_per_buyer
    return (customer_id_spent_most, most_money_spent)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    sales.get_customer_id_by_sale_id()


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
