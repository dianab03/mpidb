import random
import time
import threading

def sort_algo(algo_name, arr):
    start_time = time.time()
    if algo_name == "selection_sort":
        selection_sort(arr)
    elif algo_name == "bubble_sort":
        bubble_sort(arr)
    elif algo_name == "insertion_sort":
        insertion_sort(arr)
    elif algo_name == "merge_sort":
        merge_sort(arr)
    elif algo_name == "quick_sort":
        quick_sort(arr)
    elif algo_name == "radix_sort":
        radix_sort(arr)
    end_time = time.time()
    print(algo_name + " time: {:.6f} seconds\n".format(end_time - start_time))

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left_half = [elem for elem in arr[:-1] if elem < pivot]
    right_half = [elem for elem in arr[:-1] if elem >= pivot]

    return quick_sort(left_half) + [pivot] + quick_sort(right_half)

def counting_sort(arr, exp):
    n = len(arr)

    count = [0] * 10
    output = [0] * n

    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit]-1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]

def find_max_elem(arr):
    max_elem = arr[0]
    for elem in arr:
        if elem > max_elem:
            max_elem = elem
    return max_elem

def radix_sort(arr):
    max_elem = find_max_elem(arr)
    exp = 1
    while max_elem // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

def main():
    size = int(input("Enter the size of the array: "))

    array = [random.randint(1, 1000000) for i in range(size)]

    selection_sort_thread = threading.Thread(target=sort_algo, args=("selection_sort", array))
    bubble_sort_thread = threading.Thread(target=sort_algo, args=("bubble_sort", array))
    insertion_sort_thread = threading.Thread(target=sort_algo, args=("insertion_sort", array))
    merge_sort_thread = threading.Thread(target=sort_algo, args=("merge_sort", array))
    quick_sort_thread = threading.Thread(target=sort_algo, args=("quick_sort", array))
    radix_sort_thread = threading.Thread(target=sort_algo, args=("radix_sort", array))

    insertion_sort_thread.start()
    merge_sort_thread.start()
    quick_sort_thread.start()
    radix_sort_thread.start()
    selection_sort_thread.start()
    bubble_sort_thread.start()

    insertion_sort_thread.join()
    merge_sort_thread.join()
    quick_sort_thread.join()
    radix_sort_thread.join()
    selection_sort_thread.join()
    bubble_sort_thread.join()

if __name__ == "__main__":
    main()
