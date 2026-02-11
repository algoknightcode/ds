def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - arr[i] - left_sum

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


# Example
arr = [1, 7, 3, 6, 5, 6]
print(equilibrium_index(arr))   # Output = 3