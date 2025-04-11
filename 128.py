def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0
    for num in numSet:
        if num-1 not in numSet:
            next_num = num+1
            length = 1
            while next_num in numSet:
                length += 1
                next_num += 1
            longest = max(length, longest)

    return longest



print(longestConsecutive([100,4,200,1,3,2]))
