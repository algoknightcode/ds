#def countSubarrays(arr, k):
def countSubarrays(arr, k):
    n = len(arr)
    count = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                count += 1

    return count


arr = [3, 2, 0]
k = 2
print(countSubarrays(arr, k))   # 2