# move zeros to the end in the array 

arr = [10, 5, 0, 0, 8, 0, 9, 0]
n = len(arr)

for i in range(n):

    if arr[i] == 0:                 #if zero found

        for j in range(i+1,n):      # search for the next zero in the array 
            if arr[j]!=0:
                arr[i],arr[j] = arr[j],arr[i]
                break

print(arr)



arr = [10, 5, 0, 0, 8, 0, 9, 0]

count = 0   # position for next non-zero

for i in range(len(arr)):

    if arr[i] != 0:
        arr[i], arr[count] = arr[count], arr[i]   # swap
        count += 1

print(arr)