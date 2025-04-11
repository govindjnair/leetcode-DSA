def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []
    i = 0
    n = len(nums)
    res = []
    start = nums[0]
    while i < n:
        if i == n-1:
            if nums[i] > start:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(f"{nums[i]}")
            return res

        if nums[i] + 1 != nums[i+1]:
            if nums[i] > start:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(f"{nums[i]}")
            i += 1
            start = nums[i]
        else:
            i += 1

    return res




print(summaryRanges(nums = [0,2,3,4,6,8,9]))





