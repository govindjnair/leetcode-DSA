import time

A = [78, 5, 6, -5, 56, 34, 2, 1, 67]


def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    print(f"L is {L}")
    print(f"R is {R}")
    time.sleep(5)

    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)
    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        print(sorted_arr)
        time.sleep(10)
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        print(sorted_arr)
        time.sleep(10)
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        print(sorted_arr)
        time.sleep(10)
        r += 1
        i += 1

    return sorted_arr


result = merge_sort(A)
print(result)




