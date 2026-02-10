def min_group_flips(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            if arr[i] != arr[0]:
                print("Flip from", i, "to", end=" ")
            else:
                print(i-1)

arr = [1,1,0,0,0,1,1,0,1]
min_group_flips(arr)