from collections import Counter


def majorityElement(nums: list[int]) -> int:
    # num_counter = Counter(nums)
    # print(num_counter)
    # majority_element_count = 0
    # majority_element = None
    # for item in num_counter:
    #     if num_counter[item] > majority_element_count:
    #         majority_element_count = num_counter[item]
    #         majority_element = item
    #
    # return majority_element

    ans = 0
    count = 0
    for num in nums:
        if count == 0:
            ans = num

        if ans == num:
            count += 1
        else:
            count -= 1

    return ans

print(majorityElement([2,2,1,1,1,2,2]))
