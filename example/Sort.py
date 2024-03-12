import random

def bubble_sort(a, ascending=True):
    """
    Sorts the list 'a' using bubble sort.
    :param a: List of integers
    :param ascending: True for ascending order, False for descending order
    """
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

def main():
    random_numbers = random.sample(range(-100, 100), 10)
    print("Original set:", random_numbers)

    bubble_sort(random_numbers)
    print("Sorted set (ascending):", random_numbers)

    bubble_sort(random_numbers, ascending=False)
    print("Sorted set (descending):", random_numbers)

if __name__ == "__main__":
    print("Welcome to Bubble Sort!")
    main()
