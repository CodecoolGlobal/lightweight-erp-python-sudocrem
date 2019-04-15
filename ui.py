""" User Interface (UI) module """


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
    # Get longest elements of each column
    columns = len(table[0])
    longest_elements = [0] * columns
    for column in range(columns):
        max_column_length = 0
        for line in table:
            column_element = line[column]
            if len(column_element) > max_column_length:
                max_column_length = len(column_element)
        # Handle long headers
        if max_column_length < len(title_list[column]):
            longest_elements[column] = len(title_list[column])
        else:
            longest_elements[column] = max_column_length
    # Calculate opening and closing string
    opening_string = f"/{'-' * (sum(longest_elements) + columns * 5 - 1)}\\"
    closing_string = f"\\{'-' * (sum(longest_elements) + columns * 5 - 1)}/"
    # Create seperating lines
    sep_lines = []
    for column in longest_elements:
        sep_lines.append('-'*(column + 4))
    # Print table
    # Print headers
    print(opening_string)
    headers = []
    for index, element in enumerate(title_list):
        # Add centered element to list
        headers.append(element.center(longest_elements[index], ' '))
    print(f"|  {'  |  '.join(headers)}  |")
    print(f"|{'|'.join(sep_lines)}|")
    # Print body
    for line in table:
        centered_line = []
        for index, element in enumerate(line):
            # Add centered element to list
            centered_line.append(element.center(longest_elements[index], ' '))
        print(f"|  {'  |  '.join(centered_line)}  |")
        # Break on last element
        if line == table[-1]:
            break
        print(f"|{'|'.join(sep_lines)}|")
    # Print footer
    print(closing_string) 


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
        inputs.append(input(f"{label}: "))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code