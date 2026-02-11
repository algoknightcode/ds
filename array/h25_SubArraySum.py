# sum is given return true if it statisfy the in the subbarray of the array

arr = [3, 2, 0, 4, 7]
target = 6
n= len(arr)

def is_subarray_Sum(arr, target):
    for i in range(n): 
        curr = 0             #reset sum at every new i
        for j in range(i,n):
            curr = curr + arr[j]

            if curr == target:
                return True
        
    return False
    

print(is_subarray_Sum(arr, target))