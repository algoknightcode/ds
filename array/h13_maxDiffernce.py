#maximum diifernce  
# arr = [2, 3, 10, 6, 4, 8, 1]
# Goal → max(arr[j] - arr[i]) where j > i
# Answer → 8   (10 - 2)

arr = [2, 3, 10, 6, 4, 8, 1]
n = len(arr)

res = arr[1]-arr[0]

for i in range(n-1):
    for j in range(i+1,n):
        res = max( res, arr[j]- arr[i]) # if we dont write max it wont br able to store that it would just take diiferce every time