#deletion from the array

arr = [10,20,30,40,50]
pos = 2

for i in range(pos, len(arr)-1):
    arr[i] = arr[i+1]
    
arr.pop()
print(arr)