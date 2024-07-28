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

from random import choices

from module_ListFunction import *

list1 = choices(range(-50, 50), k=30)
list2 = choices(range(0, 150), k=30)

func_dict = {
    "max": max_value,
    "min": min_value,
    "sum": sum_values,
    "avg": avg_values,
    "median": median_value,
}

print(f"\nList: {list1}")
for func_name, func in func_dict.items():
    print(f"{func_name.title()} of list: {func(list1)}")

print(f"\nList: {list2}")
for func_name, func in func_dict.items():
    print(f"{func_name.title()} of list: {func(list2)}")
