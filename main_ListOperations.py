from random import choices, randint

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
