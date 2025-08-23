# Mergesort
import time

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = mergeSort(arr[:mid])
    right_sorted = mergeSort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1

    result.extend(left_sorted[i:])
    result.extend(right_sorted[j:])

    return result

