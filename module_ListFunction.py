"""1. (a) Develop a module called module_ListFunction that includes the following functions:
i. A function to find the maximum value in a given list.
ii. A function to find the minimum value in a given list.
iii. A function to calculate the sum of all elements in a list.
iv. A function to compute the average of the list.
v. A function to determine the median of a list.
Additionally, create lists using Python comprehension for various scenarios and demonstrate
the use of the module functions with these lists.
(b) Create another script named 'main_ListOpeartions.py' and Imports the
'module_ListFunction' to it.
(c) Demonstrate the execution of each function with suitable examples."""


def max_value(items: list):
    """Find the maximum value in the list

    Args:
        items (list): The list of values

    Returns:
        The max value
    """

    return max(items)


def min_value(items: list):
    """Find the minimum value in the list

    Args:
        items (list): The list of values

    Returns:
        The minimum value
    """

    return min(items)


def sum_values(items: list):
    """Find the sum of values

    Args:
        items (list): The list of values

    Returns:
        The sum of values
    """

    return sum(items)


def avg_values(items: list):
    """Find the average of values

    Args:
        items (list): The list of values

    Returns:
        float: The average of values
    """

    return sum(items) / len(items)


def median_value(items: list):
    """Find the median of given list

    Args:
        items (list): The list of values

    Returns:
        The median value
    """

    items.sort()
    n = len(items)
    if n % 2 == 0:
        median = items[n // 2 - 1] + items[n // 2]
    else:
        median = items[n // 2]
    return median


if __name__ == "__main__":
    # * Create a dict of functions to make calling easy
    func_dict = {
        "max": max_value,
        "min": min_value,
        "sum": sum_values,
        "avg": avg_values,
        "median": median_value,
    }

    list1 = [i for i in range(-10, 20)]
    print(f"\nList: {list1}")
    for func_name, func in func_dict.items():
        print(f"{func_name.title()} of list: {func(list1)}")

    list2 = [i * i for i in range(-5, 25)]
    print(f"\nList: {list2}")
    for func_name, func in func_dict.items():
        print(f"{func_name.title()} of list: {func(list2)}")

    list2 = [3 * i - 5 for i in range(-5, 25)]
    print(f"\nList: {list2}")
    for func_name, func in func_dict.items():
        print(f"{func_name.title()} of list: {func(list2)}")
