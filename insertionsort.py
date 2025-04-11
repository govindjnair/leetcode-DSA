A = [78, 5, 6, -5, 56, 34, 2, 1, 67]


def insertion(arr):
    n = len(arr)
    print(arr)
    for i in range(1, n):
        print(f"i = {i}")
        for j in range(i, 0, -1):
            print(f"j = {j}")
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                print(arr)
            else:
                break


insertion(A)
print(A)
