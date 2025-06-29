"""
This python file contains my self written implementation of selection sort based on books explanation.
"""

def selection_sort(arr, reverse = False):
    """
    sorting : rearranging the elements in the array/list to get ascending/descending order
    selecting sort algorithm : way to rearrange the list to get sorted list
    Worst Time complexity : O(n^2)

    :param arr: list/array of size n
    :return: sorted list of same size
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if not reverse and arr[j] < arr[min_index]:
                min_index = j
            elif reverse and arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


array = [6, 9, 7, 3, 1, 0, 2, 4, 8, 5]
sorted_array = selection_sort(array)
print("Sorted Array (Ascending): ", sorted_array)

sorted_array = selection_sort(array, reverse=True)
print("Sorted Array (Descending): ", sorted_array)
