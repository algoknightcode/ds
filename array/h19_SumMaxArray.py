# to print the max sub array is the 

arr = [1, 2, 3, 4, 5]
n = len(arr)

maxSum = 0

for st in range(n):
    currSum =0 
    for end in range(st,n):
        currSum +=arr[end]
        maxSum = max(currSum,maxSum)

print("max subarray", maxSum)