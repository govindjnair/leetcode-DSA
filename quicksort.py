A = [78, 5, 6, -5, 56, 34, 2, 1, 67]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p = arr[-1]
    print(f"pivot = {p}")
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]
    print(L)
    print(R)
    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R


result = quick_sort(A)
print(result)
