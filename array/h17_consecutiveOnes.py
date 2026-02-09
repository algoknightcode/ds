# consecutive ones

arr = [1, 0, 1, 1, 1, 0, 1]

res =  0   # max consecutive 1s
curr = 0  # current streak

for i in arr:
    if i == 0:
        curr = 0
    else:
        curr +=1
        res = max(res,curr). # just to keep the track of the variable value which can change we need another varible and why max because it can retain the value 

print(res)