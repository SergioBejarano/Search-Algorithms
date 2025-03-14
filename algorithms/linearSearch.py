
def linear_search(arr, target):
    """
    Performs a linear search on the array to find the target element.

    Args:
        arr (list): The list of elements to search.
        target: The element to find in the array.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Time Complexity: O(n), where n is the number of elements in the array.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the target is not found
