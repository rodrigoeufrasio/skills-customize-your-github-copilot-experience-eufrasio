# 📘 Assignment: Intro to Algorithms with Python

## 🎯 Objective

Learn algorithmic problem solving by implementing search and sorting patterns in Python and using a common library to visualize results.

## 📝 Tasks

### 🛠️ Implement Linear Search

#### Description
Write a function called `linear_search()` that searches a list for a target value and returns its index.

#### Requirements
Completed program should:

- Accept a list of numbers and a target value as input.
- Return the index of the target if found, or `-1` if it is not in the list.
- Example usage:
  ```python
  print(linear_search([4, 7, 1, 9], 7))  # 1
  print(linear_search([4, 7, 1, 9], 5))  # -1
  ```

### 🛠️ Implement Bubble Sort

#### Description
Write a function called `bubble_sort()` that sorts a list of numbers in ascending order.

#### Requirements
Completed program should:

- Accept a list of numbers and return a new sorted list.
- Use the bubble sort algorithm with repeated passes.
- Example usage:
  ```python
  print(bubble_sort([3, 1, 4, 2]))  # [1, 2, 3, 4]
  ```

### 🛠️ Visualize Algorithm Performance

#### Description
Write a script called `plot_search_times()` that measures how long search operations take on lists of different sizes and plots the results using `matplotlib`.

#### Requirements
Completed program should:

- Generate several lists of increasing size.
- Measure the time taken to search each list using `linear_search()`.
- Plot list size vs. search time using `matplotlib`.
- Example output: a line chart showing search time increasing as list size grows.
