# remove duplicate from thw array 

def remove_duplicate(arr):
    n= len(arr)
    res =1 # first elment will always be the sorted 

    for i in range(1,n):

        if arr[i] != arr[res-1]:      #compare current with laast unique 
            arr[res] = arr[i]         # move pointer
            res+=1
    return res                       # no of unique elemets 

arr = [10, 20, 20, 30, 30, 30]
new_size = remove_duplicate(arr)

print(remove_duplicate(arr))
print("Unique elements:", arr[:new_size])