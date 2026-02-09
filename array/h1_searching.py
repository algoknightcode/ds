# Searching in the array 

arr = [10,20,30,40]
target = 30

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # incex found at the elment x
    return-1

#example 

result = linear_search(arr, target)

if result != -1:
    print("element found at index" ,result)