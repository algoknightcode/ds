# to find the the largest subarray in  ( a)
# Find the longest subarray where numbers are alternating EVEN → ODD → EVEN → ODD … (or ODD → EVEN → ODD → EVEN).

# Example:
# [5, 10, 20, 6, 3, 8] → Answer = 3 ([6,3,8])

# 👉 If current number parity different from previous → extend length
# 👉 Else → reset length to 1

arr = [5, 10, 20, 6, 3, 8]

maxLen = 1
currLen = 1

for i in range(1, len(arr)):
    if ((arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or
        (arr[i] % 2 != 0 and arr[i-1] % 2 == 0)):
        currLen += 1
        maxLen = max(maxLen, currLen)
    else:
        currLen = 1

print("maximum length =", maxLen)