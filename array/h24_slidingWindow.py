# sliding window topic NAIVE APPROACH 

arr = [10, 5, -2, 20, 1]
k = 3
n = len(arr)


def max_sum_navive(arr, k):
    res = 0

    for i in range(n-k+1):  # this ensures that the staring index would only have 0,1,2 (index that;s all)
        curr = 0            # reset for the every window 
        for j in range(k):  # as this is inside the loop do j will only have 1,2,3
            curr += arr[i+j] 
        
        res = max(res,curr)
    
    return res

print(max_sum_navive(arr,3))



def max_sum_sliding(arr, k):    
    curr = 0          # step1 first window sum
    for i in range(k):
        curr += arr[i]

    res = curr       #best ans so far 

    #step2 slide the window
    for i in range(k,n):
        curr = curr+ arr[i] - arr[i-k]
        res = max(res, curr)

    return res

arr = [10, 5, -2, 20, 1]
k = 3
print(max_sum_sliding(arr, k))