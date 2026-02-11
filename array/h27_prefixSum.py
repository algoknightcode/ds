def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n

    prefix[0] = arr[0]   # first element same

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix


# Example
arr = [4, 8, 12, 5]
print(prefix_sum(arr))