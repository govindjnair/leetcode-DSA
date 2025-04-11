def findClosestNumber(nums: list[int]) -> int:
    n = len(nums)
    closest = nums[0]
    for i in range(1, n):
        if abs(nums[i]) < abs(closest):
            closest = nums[i]

    if abs(closest) in nums:
        return abs(closest)
    else:
        return closest

# time: O(n)
#space = O(1)

print(findClosestNumber([-4, -2, 1, 4, 8]))
