import time
import pandas as pd
from algorithms.linearSearch import linear_search
from algorithms.binarySearch import binary_search
from algorithms.ternarySearch import ternary_search
from utils.data_generator import get_random_list

def measure_execution_time(algorithm, data):
    """
    Measures the execution time of a sorting algorithm.

    :param algorithm: Sorting function.
    :param data: List to be sorted.
    :return: Execution time in seconds.
    """
    target = data[-1]
    start_time = time.perf_counter()
    algorithm(data, target)
    end_time = time.perf_counter()
    return end_time - start_time

def gather_execution_times(min_size, max_size, step, samples_per_size):
    """
    Collects execution times for different input sizes.

    :param min_size: Minimum list size.
    :param max_size: Maximum list size.
    :param step: Step size for increasing list size.
    :param samples_per_size: Number of samples per size.
    :return: Pandas DataFrame with execution times.
    """
    results = []

    for size in range(min_size, max_size + 1, step):
        aux1 = []
        aux2 = []
        aux3 = []
        print("Computing size "+str(size))
        for _ in range(samples_per_size):
            data = get_random_list(size)
            aux1.append(measure_execution_time(linear_search, data))
            aux2.append(measure_execution_time(binary_search, data))
            aux3.append(measure_execution_time(ternary_search, data))
        aux1.sort()
        aux2.sort()
        aux3.sort()
        results.append({
            'Size': size,
            'Linear Search': aux1[samples_per_size//2],
            'Binary Search': aux2[samples_per_size//2],
            'Ternary Search': aux3[samples_per_size//2]
        })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
