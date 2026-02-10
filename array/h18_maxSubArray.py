# maximum sub array - sub array formula (n*(n+1))/2

arr= [1,2,3,4,5]
n = len(arr)

for st in range(n):
    for end in range(st,n):
        for i in range(st,end+1):
            print(arr[i],end="")
        print('',end=" ")
    print()