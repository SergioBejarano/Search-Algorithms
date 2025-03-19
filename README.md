## Algorithms

### 1. Linear Search
- **Description**: Linear Search iterates through each element in the array until it finds the target element.
- **Time Complexity**: \( O(n) \)
- **Best Use Case**: Works on both sorted and unsorted arrays.
- **Implementation**: See [`algorithms/linearSearch.py`](algorithms/linearSearch.py).

### 2. Binary Search
- **Description**: Binary Search works on sorted arrays by repeatedly dividing the search interval in half.
- **Time Complexity**: \( O(\log n) \)
- **Best Use Case**: Efficient for large, sorted arrays.
- **Implementation**: See [`algorithms/binarySearch.py`](algorithms/binarySearch.py).

### 3. Ternary Search
- **Description**: Ternary Search is similar to Binary Search but divides the array into three parts instead of two.
- **Time Complexity**: \( O(\log_3 n) \)
- **Best Use Case**: Useful for unimodal functions or when searching in sorted arrays.
- **Implementation**: See [`algorithms/ternarySearch.py`](algorithms/ternarySearch.py).


## 🛠 How to Use

## ✅ Run tests with coverage

```sh
coverage run -m unittest discover -s tests
```

## 📊 Generate coverage report:
```sh
coverage report -m
```

##  Executing the Main Script
```sh
python main.py
```

Example:

![image](https://github.com/user-attachments/assets/356946bf-4ba2-43f8-b68f-f92e92df7296)

![image](https://github.com/user-attachments/assets/cfcb7e1a-3a14-44d1-a927-9bd2545119b4)


