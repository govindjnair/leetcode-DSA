def two_sum(arr, target):
    # index_dict = {}
    # result = []
    # for i, number in enumerate(arr):
    #     complement = target - number
    #     if complement in index_dict:
    #         result.append([index_dict[complement], i])
    #     index_dict[number] = i
    # return result

    h = {}
    for i in range(len(arr)):
        h[arr[i]] = i

    for i in range(len(arr)):
        y = target - arr[i]
        if y in h and h[y] != i:
            return [i, h[y]]

result = two_sum([3, 2, 2, 3], 6)
print(result)
