import time

def measure_time(algorithm, arr, target):
    """
    Measures the execution time of a search algorithm.

    Args:
        algorithm (function): The search algorithm function to measure.
        arr (list): The array in which to perform the search.
        target: The element to search for.

    Returns:
        float: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(arr, target)
    end_time = time.time()
    return end_time - start_time