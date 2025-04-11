A = [78, 5, 6, -5, 56]


def bubble(arr):
    n = len(arr)
    flag = True
    print(arr)
    while flag:
        flag = False
        for i in range(1, n):
            print(f"i = {i}")
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                print(arr)


bubble(A)
print(A)
