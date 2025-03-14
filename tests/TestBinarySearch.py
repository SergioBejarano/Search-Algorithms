import unittest
from algorithms.binarySearch import binary_search


class TestBinarySearch(unittest.TestCase):
    """
    Unit tests for the Binary Search algorithm.
    """
    def test_element_found(self):
        arr = [3, 5, 7, 9, 11, 13]
        target = 9
        result = binary_search(arr, target)
        self.assertEqual(result, 3)  # Element is at index 3

    def test_element_not_found(self):
        arr = [3, 5, 7, 9, 11, 13]
        target = 8
        result = binary_search(arr, target)
        self.assertEqual(result, -1)  # Element not found

    def test_empty_array(self):
        arr = []
        target = 5
        result = binary_search(arr, target)
        self.assertEqual(result, -1)  # Empty array

    def test_single_element_found(self):
        arr = [5]
        target = 5
        result = binary_search(arr, target)
        self.assertEqual(result, 0)  # Single element found at index 0

    def test_single_element_not_found(self):
        arr = [5]
        target = 10
        result = binary_search(arr, target)
        self.assertEqual(result, -1)  # Single element not found