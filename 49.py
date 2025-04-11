from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)
        anagrams_dict[key].append(s)
    print(anagrams_dict)
    return list(anagrams_dict.values())


print(groupAnagrams(strs= ["eat","tea","tan","ate","nat","bat"]))