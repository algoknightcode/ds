arr = [8, -4, 3, -5, 4]

# 1. Normal Kadane (max subarray)
currMax = maxSum = arr[0]
for i in range(1, len(arr)):
    currMax = max(arr[i], currMax + arr[i])
    maxSum = max(maxSum, currMax)

# 2. Find minimum subarray sum (Kadane for min)
currMin = minSum = arr[0]
for i in range(1, len(arr)):
    currMin = min(arr[i], currMin + arr[i])
    minSum = min(minSum, currMin)

totalSum = sum(arr)

# 3. Circular max
circularMax = totalSum - minSum

# 4. Handle all-negative case
if maxSum < 0:
    print("Max circular sum =", maxSum)
else:
    print("Max circular sum =", max(maxSum, circularMax))