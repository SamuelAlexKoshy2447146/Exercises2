"""3. Write a program to create functions that can accept multiple dictionaries 
as arguments using '*args', and perform various operations on them.
(a) Write a function, say, 'merging_Dict(*args)' that takes multiple 
dictionaries and merge them.

(b) Write a function which can find common keys in multiple dictionaries.

(c) Create a function to invert a dictionary, swapping keys and values. If multiple keys have
the same value, group these keys in a list in the inverted dictionary. Implement and demonstrate
this with examples.

(d)Write a function to find common key-value pairs across multiple dictionaries.
"""


def merging_dict(*args):
    """Merge any number of dictionaries

    Returns:
        dict: The new dictionary
    """

    new_dict = dict()
    for item in args:
        if isinstance(item, dict):  # Ignore if not a dict
            new_dict.update(item)
    return new_dict


def common_keys(*args):
    """Find common keys in dictionaries

    Returns:
        dict: The keys that are common with the count of how many times they apppeared
    """

    keys = dict()
    for item in args:
        if isinstance(item, dict):  # Ignore if not a dict
            for key in item:
                if key in keys:  # Check if key already found
                    keys[key] += 1
                else:
                    keys[key] = 1
    return {
        key: value for key, value in keys.items() if value > 1
    }  # Display only keys that have duplicates


def invert_dict(dictionary: dict):
    """Invert keys and values of a dict, and if there are multiple values,
    put it in a list

    Args:
        dictionary (dict): The dictionary to be inverted

    Returns:
        dict: The new inverted dictionary
    """

    inverted_dict = dict()
    for key, value in dictionary.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
        elif type(inverted_dict[value]) is list:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [inverted_dict[value], key]
    return inverted_dict


def common_key_value(*args):
    """Find common key value pairs across dictionaries

    Returns:
        dict: The dict contains keys and values that have repeated
    """

    new_dict = {}
    common_dict = {}
    for item in args:
        if isinstance(item, dict):  # Ignore if not a dict
            for key, value in item.items():
                if key not in new_dict:
                    new_dict[key] = value
                elif new_dict[key] == value:
                    if key in common_dict:
                        common_dict[key] += 1
                    else:
                        common_dict[key] = 1
    return {key: new_dict[key] for key in common_dict}


if __name__ == "__main__":
    dict1 = {"name": "Sam", "age": 3}
    dict2 = {"color": "brown", "school": "Christ"}
    print("Dict1:", dict1)
    print("Dict2:", dict2)
    print("Merging dictionaries:", end=" ")
    print(merging_dict(dict1, dict2))
    dict3 = {"color": "blue", "class": "MCA"}
    print("Dict3:", dict3)
    print("Merging dictionaries", merging_dict(dict1, dict2, dict3))
    list1 = ["name", "age", "talent"]
    set1 = {7, 9, "Sam"}
    print("List: ", list1)
    print("Set:", set1)
    print("Merging everything:", merging_dict(dict1, dict2, dict3, list1, set1))

    print("Common keys:", common_keys(dict1, dict2, dict3))
    merged_dict = merging_dict(dict1, dict2, dict3)
    print("Inverted dictionary:", invert_dict(merged_dict))
    dict4 = {"name": "Sam", "age": 22, "roll": 22, "color": "blue"}
    print("Dict 4:", dict4)
    print("Inverted dictionary:", invert_dict(dict4))
    print("Common keys and values:", common_key_value(merged_dict, dict4))
