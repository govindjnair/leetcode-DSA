def checkInclusion(s1: str, s2: str) -> bool:
    l = 0
    n = len(s2)
    k = len(s1)
    counts1 = [0] * 26
    counts2 = [0] * 26

    for c in s1:
        counts1[ord(c) - 97] += 1

    for r in range(n):
        while r - l + 1 > k:
            counts2[ord(s2[l]) - 97] -= 1
            l += 1

        counts2[ord(s2[r]) - 97] += 1
        if counts1 == counts2:
            return True

    return False


print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))







