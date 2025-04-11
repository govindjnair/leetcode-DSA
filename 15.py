def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i] > 0:  # if the number is positive, so the sum would be positive as high and low would be positive
            break
        elif i > 0 and nums[i] == nums[i - 1]:  # same value as the previous number, to avoid duplicates
            continue

        low, high = i+1, n-1
        while low < high:
            current_sum = nums[i] + nums[low] + nums[high]
            if current_sum == 0:
                answer.append([nums[i], nums[low], nums[high]])
                low, high = low+1, high-1
                while low < high and nums[low] == nums[low-1]:
                    low += 1
                while low < high and nums[high] == nums[high+1]:
                    high -= 1

            elif current_sum < 0:
                low += 1
            else:
                high -= 1

    return answer



print(threeSum(nums = [-1,0,1,2,-1,-4]))