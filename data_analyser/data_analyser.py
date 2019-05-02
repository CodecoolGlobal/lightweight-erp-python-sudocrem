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


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Last buyer's name",
               "Last buyer's ID",
               "Customer's name who spent most & amount",
               "Customer's ID who spent most & amount",
               "Most frequent buyers names",
               "Most frequent buyers ID's"
               ]

    while True:
        ui.print_menu("Data analyser menu", options, "Go back to main")
        
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            ui.print_result(get_the_last_buyer_name(), "Last buyer's name")
        elif option == "2":
            ui.print_result(get_the_last_buyer_id(), "Last buyer's ID")
        elif option == "3":
            ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(), "Customer's name who spent most & amount")
        elif option == "4":
            ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(), "Customer's ID who spent most & amount")
        elif option == "5":
            ui.print_result(get_the_most_frequent_buyers_names(), "Most frequent buyers names")
        elif option == "6":
            ui.print_result(get_the_most_frequent_buyers_ids(), "Most frequent buyers ID's")
        elif option == "0":
            return None
        else:
            raise KeyError("There is no such option.")



def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    customer_id = get_the_last_buyer_id()
    customer_name = crm.get_name_by_id(customer_id)
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

    for customer_id, sale_ids in all_sales_ids_for_customer_ids.items():
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

    # your code


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
