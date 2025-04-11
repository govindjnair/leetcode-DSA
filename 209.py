def minSubArrayLen(target: int, nums: list[int]) -> int:
    l = 0
    n = len(nums)
    s = 0
    mini = float("inf")

    for r in range(n):
        s += nums[r]
        while s >= target:
            w = r - l + 1
            mini = min(w, mini)
            s -= nums[l]
            l += 1

    return mini if mini < float("inf") else 0


print(minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
