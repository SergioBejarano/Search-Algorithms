import matplotlib.pyplot as plt
import pandas as pd
from utils.data_generator import generate_sorted_array
from utils.time_capture import measure_time
from algorithms.linearSearch import linear_search
from algorithms.binarySearch import binary_search
from algorithms.ternarySearch import ternary_search

def main():

    sizes = [2000000 * i for i in range(1, 30)]  # Array sizes
    results = {"Size": sizes, "Linear Search": [], "Binary Search": [], "Ternary Search": []}

    # Time measurement
    for size in sizes:
        print("Processing "+str(size))
        arr = generate_sorted_array(size)
        target = size - 1  # Search for the last element (worst case for linear search)

        linear_time = measure_time(linear_search, arr, target)
        binary_time = measure_time(binary_search, arr, target)
        ternary_time = measure_time(ternary_search, arr, target)

        results["Linear Search"].append(linear_time)
        results["Binary Search"].append(binary_time)
        results["Ternary Search"].append(ternary_time)

    df = pd.DataFrame(results)

    plt.figure(figsize=(10, 6))
    plt.plot(df["Size"], df["Linear Search"], label="Linear Search", marker="o")
    plt.plot(df["Size"], df["Binary Search"], label="Binary Search", marker="o")
    plt.plot(df["Size"], df["Ternary Search"], label="Ternary Search", marker="o")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Search Algorithms Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()