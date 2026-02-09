# arr = [10, 10, 10, 25, 25, 30, 30, 30, 30]
# Output:
# 10 → 3
# 25 → 2
# 30 → 4

arr = [10, 10, 10, 25, 25, 30, 30, 30, 30]
n = len(arr)

count = 1

for i in range(1,n):
    if arr[i] == arr[i-1]:
        count+=1
    else:
        print(arr[i-1], "->", count)
        count=1
print(arr[n-1], "→", count)