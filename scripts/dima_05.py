"""Bubble sort utility."""


def bubble_sort(items):
    arr = list(items)
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 7]))
