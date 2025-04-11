def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    # shortest = min(strs, key=len)
    # length = len(shortest)
    # # print(shortest)
    # # print(length)
    #
    length = float("inf")
    shortest = None
    for item in strs:
        if len(item) < length:
            length = len(item)
            shortest = item

    for i in range(length):
        for s in strs:
            if s[i] != shortest[i]:
                return res
        res += shortest[i]

    return res


print(longestCommonPrefix(strs=["flower","flow","flight"]))


# print(longestCommonPrefix(strs=[""]))
# print(longestCommonPrefix(strs=["dog", "racecar", "car"]))
