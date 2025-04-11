# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


def firstBadVersion(n: int) -> int:
    L = 1
    R = n
    while L < R:
        M = (L + R) // 2
        if isBadVersion(M):
            R = M
        else:
            L = M + 1

    return L


