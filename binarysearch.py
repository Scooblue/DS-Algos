def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return comparisons
