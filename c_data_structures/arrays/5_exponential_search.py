def binary_search(nums, n, lo=0, hi=None):
    if hi is None:
        hi = len(nums)-1

    while lo < hi:
        mid = int((lo+hi)/2)
        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1

    while i < n and arr[i] < target:
        i *= 2

    if arr[i] == target:
        return i

    return binary_search(arr, target, i//2, min(i, n-1))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = exponential_search(a, target)

print(f'element found at index {result}')
