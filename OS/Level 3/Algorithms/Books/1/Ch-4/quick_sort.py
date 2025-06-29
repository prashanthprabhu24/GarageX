"""
This python file contains my self written implementation of quick sort based on books explanation.
"""


def quick_sort(arr, reverse = False):
    """
    sorting : rearranging the elements in the array/list to get ascending/descending order.
    quick sort algorithm : way to rearrange the list to get sorted list
    Worst Time complexity : O(n^2), O(n Log n) based on pivot

    :param arr: list/array of size n
    :return: sorted list of same size
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    if reverse:
        return quick_sort(greater, reverse) + [pivot] + quick_sort(less, reverse)
    return quick_sort(less) + [pivot] + quick_sort(greater)


array = [6, 9, 7, 3, 1, 0, 2, 4, 8, 5]
sorted_array = quick_sort(array)
print("Sorted Array (Ascending): ", sorted_array)

sorted_array = quick_sort(array, reverse=True)
print("Sorted Array (Descending): ", sorted_array)