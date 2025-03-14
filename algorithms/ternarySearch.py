def ternary_search(arr, target):
    """
    Performs a ternary search on a sorted array to find the target element.
    The array is divided into three parts in each iteration.

    Args:
        arr (list): The sorted list of elements to search.
        target: The element to find in the array.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Time Complexity: O(log₃ n), where n is the number of elements in the array.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Divide the array into three parts
        third1 = left + (right - left) // 3
        third2 = right - (right - left) // 3

        if arr[third1] == target:
            return third1  # Return the index of the found element
        if arr[third2] == target:
            return third2  # Return the index of the found element

        if target < arr[third1]:
            right = third1 - 1
        elif target > arr[third2]:
            left = third2 + 1
        else:
            left = third1 + 1
            right = third2 - 1

    return -1  # Return -1 if the target is not found

