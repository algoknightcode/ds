# 2nd largest in the array 
# #rules  If number > largest
# → second = largest
# → largest = number

# Else if number > second AND number != largest
# → second = number

def second_largest(arr):
    largest = arr[0]
    second = -1
    
    for i in range(1, len(arr)):
        
        if arr[i]>largest:
            second =largest
            largest = arr[i]
            
        elif arr[i] > second and arr[i] != largest:
            second = arr[i]
            
    return second

arr = [10, 20, 40, 90]
print("Second largest =", second_largest(arr))