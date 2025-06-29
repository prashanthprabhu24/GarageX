"""
This python file contains my self written implementation of sequential search based on books explanation.
"""


def sequential_search(my_list, search_key):
    """
    sequential search : search through every element in my_list list to find search_key exists.
    Work Case Time complexity : O(n) ; n-> number of element in list.

    :param my_list: list of size n
    :param search_key: an element to search
    :return: index of the search key if exists, else -1
    """
    for i, element in enumerate(my_list):
        if element == search_key:
            print(f"Search Key {search_key} exists in given list at {i} index.")
            return i
    print(f"Search Key {search_key} doesnt exist in given list.")
    return -1


my_list1 = [8, 3, 5, -1, 5, 0, -7, 9, 4, 6]

sequential_search(my_list1, 0) # Existing Key
sequential_search(my_list1, 1) # Key doesnt exists