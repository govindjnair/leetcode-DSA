def longestOnes(nums: list[int], k: int) -> int:
    max_length = 0
    num_zeroes = 0
    n = len(nums)
    l = 0

    for r in range(n):
        if nums[r] == 0:
            num_zeroes += 1

        while num_zeroes > k:
            if nums[l] == 0:
                num_zeroes -= 1
            l += 1

        length = (r - l) + 1
        max_length = max(max_length, length)

    return max_length


print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))