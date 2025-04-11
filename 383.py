from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    possible = False
    rnote = Counter(ransomNote)
    mag = Counter(magazine)
    print(ransomNote)
    print(rnote)
    print(magazine)
    print(mag)

    for char in rnote:
        if char in mag:
            if mag[char] >= rnote[char]:
                possible = True
            else:
                return False
        else:
            return False

    return possible


print(canConstruct(ransomNote = "fihjjjjei", magazine = "hjibagacbhadfaefdjaeaebgi"))