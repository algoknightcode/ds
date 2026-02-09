# reverse the array in the python 

arr = [1,2,3,45,6]

def reverse(arr):
    low =0
    high = len(arr)-1

    while low<high:
        arr[low],arr[high] = arr[high],arr[low]
        low+=1
        high-=1

    return arr

print(reverse(arr))