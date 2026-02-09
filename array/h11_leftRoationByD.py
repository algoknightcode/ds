def left_rotate(arr, d):
    n = len(arr)
    d = d % n

    temp = arr[:d]          # store first d elements

    for i in range(d, n):   # shift remaining left
        arr[i-d] = arr[i]

    for i in range(d):      # put stored at end
        arr[n-d+i] = temp[i]

    return arr


arr = [1,2,3,4,5,6,7]
print(left_rotate(arr, 2))