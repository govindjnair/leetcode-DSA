def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stk = []
    result = [0] * n

    for i in range(n):
        current_temp = temperatures[i]
        while stk and current_temp > stk[-1][0]:
            popped = stk.pop()
            result[popped[1]] = i - popped[1]

        stk.append((current_temp, i))

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
