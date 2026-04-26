def binary_search(nums, n):
    lo = 0
    hi = 0

    while lo < hi:
        mid = int((lo+hi)/2)

        if mid == n:
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid
        return -1
