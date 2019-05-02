""" User Interface (UI) module """


def get_summa(list):
    sum_ = 0
    for element in list:
        sum_ += int(element)
    return sum_


def get_longest_elements_of_each_column_in_a_table(table, column_headers):
    columns = len(column_headers)
    longest_elements = [0] * columns

    for column_index in range(columns):
        max_column_length = 0
        for line in table:
            column_element = line[column_index]
            if len(column_element) > max_column_length:
                max_column_length = len(column_element)
        
        # Handle long headers
        if max_column_length < len(column_headers[column_index]):
            longest_elements[column_index] = len(column_headers[column_index])
        else:
            longest_elements[column_index] = max_column_length
    return longest_elements


def get_separator(longest_elements, number_of_columns):
    number_of_separators = get_summa(longest_elements) + number_of_columns * 5 - 1
    return number_of_separators * '-'


def get_header(separator):
    return f"/{separator}\\"


def get_footer(separator):
    return f"\\{separator}/"


def get_middle_separator(longest_elements):
    middle_lines = []
    for column in longest_elements:
        separator_width = 4
        middle_line = '-' * (column + separator_width)
        middle_lines.append(middle_line)
    return f"|{'|'.join(middle_lines)}|"


def get_centered_line(line, longest_elements):
    centered_line = []
    for index, element in enumerate(line):
        centered_line.append(element.center(longest_elements[index], ' '))
    return (f"|  {'  |  '.join(centered_line)}  |")


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    number_of_columns = len(title_list)
    longest_elements = get_longest_elements_of_each_column_in_a_table(table, title_list)
    separator = get_separator(longest_elements, number_of_columns)
    header = get_header(separator)
    footer = get_footer(separator)
    middle_separator = get_middle_separator(longest_elements)

    print(header)
    print(get_centered_line(title_list, longest_elements))
    for line in table:
        print(middle_separator)
        print(get_centered_line(line, longest_elements))
        if line == table[-1]:
            break
    print(footer)
    print()


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f"{label}: ")
    if type(result) == str:
        print(result)
    elif type(result) == list:
        for line in result:
            print(line)
    elif type(result) == dict:
        for key in result:
            print(f"{key} : {result[key]}")
    else:
        pass
    print()


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"{title}: ")
    for index, list_option in enumerate(list_options, start = 1):
        print(f"    ({index}) {list_option}")
    print(f"    (0) {exit_message}")
    print()


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
    for label in list_labels:
        inputs.append(input(f"{label} "))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"Error: {message}")
    print()
