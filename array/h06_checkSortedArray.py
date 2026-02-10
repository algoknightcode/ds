# to check if the array id already sorted 

def is_sorted(arr):
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return False
    return True


arr= [1,2,4,5,3]

if is_sorted(arr):
    print("array is already sorted")
    
else:
    print("not sorted")