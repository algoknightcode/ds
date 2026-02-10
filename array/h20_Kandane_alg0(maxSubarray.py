# kandane algo is the most optimized appraoch to it 

arr = [3, -4, 5, 4, -1, 7, -8]

currSum = 0
maxSum = 0

for x in arr:
    currSum +=x
    maxSum = max(maxSum,currSum)

    if currSum < 0:
       currSum = 0
    
print("max subarray sum is", maxSum)