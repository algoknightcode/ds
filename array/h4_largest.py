# largest in the array 

# assume the first elemeent in the array is the largest and compare it with other

def find_largest(arr):
    largest = arr[0]
    
    for i in range(1, len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
            
    return largest
    
arr = [10,20, 40,90]
print("largest is" ,find_largest(arr))