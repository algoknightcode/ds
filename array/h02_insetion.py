# insertion at the fixed position

def insert_element(arr, pos , value):
    arr.append(0)
    
    for i in range(len(arr)-1 ,pos,-1 ):
        arr[i] =arr[i-1]
        
    arr[pos] = value
    return arr


arr = [10, 20 ,30, 40 ,50]
pos= 2
value= 25

print(insert_element(arr,pos,value))