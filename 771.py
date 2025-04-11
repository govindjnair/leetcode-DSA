from collections import Counter
def numJewelsInStones(jewels: str, stones: str) -> int:
    num = 0
    # data = Counter(stones)
    # for char in jewels:
    #     if char in data:
    #         num += data[char]
    #
    #
    # print(data)
    # print(num)
    # return num
    s = set(jewels)
    for stone in stones:
        if stone in s:
            num += 1
    print(num)
    return num






numJewelsInStones(jewels = "aA", stones = "aAAbbbb")



