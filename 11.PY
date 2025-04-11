def maxArea(height: list[int]) -> int:
    n = len(height)
    l = 0
    r = n - 1
    max_area = 0
    while l < r:
        w = r - l
        h = min(height[l], height[r])
        curr_area = w * h
        max_area = max(max_area, curr_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
