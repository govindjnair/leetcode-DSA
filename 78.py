nums = [1, 2, 3]


def subset(nums):
    n = len(nums)
    res, sol = [], []

    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return

        # don't pick nums[i]
        backtrack(i + 1)

        # pick nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()

    backtrack(0)
    return res


print(subset(nums))
