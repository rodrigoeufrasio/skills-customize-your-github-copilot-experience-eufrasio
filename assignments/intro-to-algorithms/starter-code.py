import time
import matplotlib.pyplot as plt


def linear_search(numbers, target):
    """Return the index of target in numbers or -1 if not found."""
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1


def bubble_sort(numbers):
    """Return a sorted copy of the input list using bubble sort."""
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )
    return sorted_numbers


def plot_search_times():
    """Measure linear search performance and plot results."""
    sizes = [100, 200, 400, 800, 1600]
    times = []

    for size in sizes:
        numbers = list(range(size))
        target = size - 1
        start = time.perf_counter()
        linear_search(numbers, target)
        end = time.perf_counter()
        times.append(end - start)

    plt.plot(sizes, times, marker="o")
    plt.title("Linear Search Performance")
    plt.xlabel("List size")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print(linear_search([4, 7, 1, 9], 7))
    print(bubble_sort([3, 1, 4, 2]))
    plot_search_times()
