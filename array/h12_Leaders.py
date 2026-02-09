# leaders in the array :  An element is Leader if no element to its RIGHT is greater.
#arr = [7, 10, 4, 10, 6, 5, 2, 3]
#Leaders → 10, 6, 5, 3

arr = [7, 10, 4, 10, 6, 5, 2, 3]
n = len(arr)

for i in range(n):
    flag = False
    for j in range(i+1,n):
        if arr[j] >= arr[i]:  # bigger element found at the top
            flag = True
            break
    if flag == False:
        print(arr[i],)