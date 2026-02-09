def trap(height):
    n = len(height)

    lmax = [0] * n
    rmax = [0] * n

    # same as: lmax[0] = height[0]
    lmax[0] = height[0]

    # for (i=1 → n-1)  lmax[i] = max(lmax[i-1], height[i])
    for i in range(1, n):
        lmax[i] = max(lmax[i-1], height[i])

    # same as: rmax[n-1] = height[n-1]
    rmax[n-1] = height[n-1]

    # for (i=n-2 → 0)  rmax[i] = max(rmax[i+1], height[i])
    for i in range(n-2, -1, -1):
        rmax[i] = max(rmax[i+1], height[i])

    ans = 0

    # for each index → ans += min(lmax[i], rmax[i]) - height[i]
    for i in range(n):
        ans += min(lmax[i], rmax[i]) - height[i]

    return ans


# Example (same typical test)
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))