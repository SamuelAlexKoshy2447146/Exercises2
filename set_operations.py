"""2. Write a Python program to create a module that performs various set operations.
a. Write a function to add an element to a set, ensuring no errors if the element is already
present.
b. Write a function to remove an element from a set, ensuring no errors if the element is
not present.
c. Write a function to return the union and intersection of two sets, handling empty sets
correctly.
d. Write a function to return the difference S1−S2, handling empty sets correctly.
e. Write a function to check if set S1 is a subset of set S2, handling empty sets correctly.
f. Write a function to find the length of a set without using the len() function.
g. Write a function to compute the symmetric difference of two sets.
h. Write a function to compute the power set of a given set.
i. Write a function to get all unique subsets of a given set.
Implement this module and demonstrate it by using adequate examples."""


def add_to_set(collection: set, element):
    """Add an element to a set

    Args:
        collection (set): The set to be added to
        element: The element to be added

    Returns:
        set: The new set
    """

    collection.add(element)  # ? No error even if element already exists
    return collection


def remove_from_set(collection: set, element):
    """Remove an element from the set if it exists, else return the set itself

    Args:
        collection (set): The set
        element: The element to be removed

    Returns:
        set: The new set
    """

    if element in collection:
        collection.remove(element)
    return collection


def union_and_intersection(collection_1: set, collection_2: set):
    """Find union and interesection of 2 sets

    Args:
        collection_1 (set): The first set
        collection_2 (set): The second set

    Returns:
        union: The union of the sets
        intersection: The intersection of the sets
    """

    union = collection_1.union(collection_2)
    intersection = collection_1.intersection(collection_2)
    return union, intersection


def difference_sets(collection_1: set, collection_2: set):
    """Find the difference of the sets

    Args:
        collection_1 (set): The first set
        collection_2 (set): The second set

    Returns:
        set: The difference of sets
    """

    return collection_1.difference(collection_2)


def check_subset(s1: set, s2: set):
    """Check if the first set is a subset of the second

    Args:
        s1 (set): The first set
        s2 (set): The second set

    Returns:
        bool: True if it is a subset, else False
    """

    return s1.issubset(s2)


def length_set(s1: set):
    """Find the length of the set without using len()

    Args:
        s1 (set): The set

    Returns:
        int: The length of the set
    """

    count = 0
    for _ in s1:
        count += 1
    return count


def symmetric_difference(s1: set, s2: set):
    """Find the symmetric difference of the sets

    Args:
        s1 (set): The first set
        s2 (set): The second set

    Returns:
        set: The symmetric difference of the sets
    """

    return s1.symmetric_difference(s2)


def compute_power_set(s1: set):
    """Find the power set of a set

    Args:
        s1 (set): The set

    Returns:
        set: The power set
    """

    list_set = list(s1)
    power_set = set()
    length = len(s1)
    for i in range(2**length):
        subset = set()
        bin_value = f"{bin(i)[2:].zfill(length)}"  # Convert decmial number to binary and fill with zeros
        for pos, val in enumerate(bin_value):
            if val == "1":  # If value is 1, then use that index to add to subset
                subset.add(list_set[pos])
        power_set.add(frozenset(subset))
    return power_set


def unique_subset(s1: set):
    """Find the unique subsets of a set (power set without empty set)

    Args:
        s1 (set): The set

    Returns:
        set: The set containing unique subsets
    """

    list_set = list(s1)
    power_set = set()
    length = len(s1)
    for i in range(1, 2**length):
        subset = set()
        bin_value = f"{bin(i)[2:].zfill(length)}"  # Convert decmial number to binary and fill with zeros
        for pos, val in enumerate(bin_value):
            if val == "1":  # If value is 1, then use that index to add to subset
                subset.add(list_set[pos])
        power_set.add(frozenset(subset))
    return power_set


if __name__ == "__main__":
    collection = {1, 2, 3}
    print("Original collection", collection)
    collection = add_to_set(collection, 4)
    print("After adding 4:", collection)
    collection = add_to_set(collection, 3)
    print("After adding 3:", collection)
    collection = remove_from_set(collection, 2)
    print("After removing 2:", collection)
    collection = remove_from_set(collection, 5)
    print("After removing 5:", collection)

    collection_1 = set([1, 3, -4, 81, 9])
    collection1, collection2 = union_and_intersection(collection, collection_1)
    print("Union:", collection1)
    print("Intersection:", collection2)
    collection3, collection4 = union_and_intersection(collection, set())
    print("Union:", collection3)
    print("Intersection:", collection4)

    print("Difference:", difference_sets(collection, collection2))
    print("Difference:", difference_sets(collection, set()))

    print("Check subset:", check_subset(collection_1, set()))
    print("Check subset:", check_subset(set(), collection))
    print("Length:", length_set(collection1))
    print("Symmetric difference:", symmetric_difference(collection, collection_1))

    print("Power set:", compute_power_set(collection))
    print("Unique subset:", unique_subset(collection))
