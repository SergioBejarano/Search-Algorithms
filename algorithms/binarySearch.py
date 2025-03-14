
def binary_search(arr, target):
    """
    Performs a binary search on a sorted array to find the target element.

    Args:
        arr (list): The sorted list of elements to search.
        target: The element to find in the array.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Time Complexity: O(log n), where n is the number of elements in the array.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index of the found element
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target is not found

