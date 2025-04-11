words = ["pay", "attention", "practice", "attend"]
pref = "at"

# words = ["leetcode", "win", "loops", "success"]
# pref = "code"


def prefixCount(words, pref) -> int:
    count = 0
    for word in words:
        if pref in word[:len(pref)]:
            count += 1

    return count


def test(words, pref):
    return len([1 for word in words if pref in word[:len(pref)]])


print(prefixCount(words, pref))
print(test(words, pref))