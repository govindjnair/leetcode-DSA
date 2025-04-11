A = [7, 1, 4, 3, 1]


def counting_sort(arr):
    maxx = max(arr)
    counts = [0] * (maxx + 1)
    for x in arr:
        counts[x] += 1
    print(counts)
    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1
            print(arr)
            print(counts)

    return arr


result = counting_sort(A)
print(result)
