# code for to sell and buy 
arr = [2, 3, 10, 6, 4, 8, 1]

maxProfit = 0
bestBuy = arr[0] 

for i in range(1, len(arr)):
    if arr[i]> bestBuy:
        maxProfit = max(maxProfit,arr[i]-bestBuy)

    bestBuy = min(bestBuy,arr[i])
print(maxProfit)