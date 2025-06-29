"""
This python file contains my self written implementation of binary search based on books explanation.
"""

def binary_search(my_sorted_list, search_key):
    """
    Binary Search is a fast algorithm used to find an item in a sorted list by repeatedly dividing the search range in half.
    
    :param my_sorted_list: sorted (ascending) list of size n
    :param search_key: an element to search
    :return: index of the search key if exists, else -1
    """
    low = 0
    high = len(my_sorted_list)
    while low <= high:
        mid = (low + high) // 2
        elem = my_sorted_list[mid]
        if elem > search_key:
            high = mid - 1
        elif elem < search_key:
            low = mid + 1
        else:
            print(f"Search Key {search_key} exists in given list at {mid} index.")
            return mid
    print(f"Search Key {search_key} doesnt exist in given list.")
    return -1


my_list1 = [-10, -3, 0, 2, 5, 9, 10, 12, 16, 17, 28]

binary_search(my_list1, 0)
binary_search(my_list1, 1)

