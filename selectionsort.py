A = [78, 5, 6, -5, 56, 34, 2, 1, 67]


def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"i = {i}")
        print(f"min index: {min_index}")
        for j in range(i + 1, n):
            print(f"j = {j}")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"min index: {min_index}")
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


selection(A)
