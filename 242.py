from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_counter = Counter(s)
    t_counter = Counter(t)
    if s_counter == t_counter:
        return True
    else:
        return False
