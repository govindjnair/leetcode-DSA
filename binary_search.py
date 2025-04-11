test = [-5, -4, -3, 1, 2, 4, 5, 7]


def binary_search(arr, target):
    n = len(arr)
    L = 0
    R = n - 1

    while L <= R:
        M = L + ((R - L) // 2)
        if arr[M] == target:
            return True
        elif target > arr[M]:
            L = M + 1
        else:
            R = M - 1
    return False


# result = binary_search(test, 5)
# print(result)

another = [False, False, False, False, True, True, True]


def binary_op(arr):
    n = len(arr)
    L = 0
    R = n - 1

    while L < R:
        M = L + ((R - L) // 2)
        if arr[M]:
            R = M
        else:
            L = M + 1

    return L


result = binary_op(another)
print(result)
