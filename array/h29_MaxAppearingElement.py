def max_appearing(left, right):
    freq = [0] * 100   # assuming values <= 99

    for i in range(len(left)):
        for j in range(left[i], right[i] + 1):
            freq[j] += 1
                                                  
    res = 0
    for i in range(100):
        if freq[i] > freq[res]:
            res = i

    return res


left  = [1, 2, 4]
right = [4, 5, 7]
print(max_appearing(left, right))   # Output = 4