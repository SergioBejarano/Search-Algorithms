import pandas as pd
import matplotlib.pyplot as plt
from utils.time_capture import gather_execution_times

def plot_execution_times(df):
    """
    Plots execution times of searching algorithms in two separate subplots.

    :param df: DataFrame with execution times.
    """
    plt.figure(figsize=(14, 10))

    plt.subplot(2, 1, 1)
    if 'Linear Search' in df.columns:
        plt.plot(df['Size'], df['Linear Search'], label='Linear Search', color='blue')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Linear Search Execution Time Analysis')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    for algorithm in ['Binary Search', 'Ternary Search']:
        if algorithm in df.columns:
            plt.plot(df['Size'], df[algorithm], label=algorithm)
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Binary Search and Ternary Search Execution Time Analysis')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    # Parameters
    min_size = 100000
    max_size = 10000000
    step = 500000
    samples_per_size = 80

    df = gather_execution_times(min_size, max_size, step, samples_per_size)

    print("Size | Linear Search | Binary Search | Ternary Search")
    for _, row in df.iterrows():
        print(f"{int(row['Size'])}  | {row['Linear Search']:.6f} | {row['Binary Search']:.6f} | {row['Ternary Search']:.6f}")
    plot_execution_times(df)

if __name__ == '__main__':
    main()