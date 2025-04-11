def sortedSquares(nums): # two pointers
    left = i = 0
    right = j = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    # result.reverse()
    while i <= j:
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1

    return result


# print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7, -3,2, 3, 11]))





