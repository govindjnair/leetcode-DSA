def containsDuplicate(nums: list[int]) -> bool:
    # counter = {}
    # for n in nums:
    #     if n in counter:
    #         counter[n] += 1
    #         return True
    #     else:
    #         counter[n] = 1
    #
    # return False
    h = set()
    for n in nums:
        if n in h:
            return True
        else:
            h.add(n)

    return False




print(containsDuplicate(nums = [1,2,3,1]))