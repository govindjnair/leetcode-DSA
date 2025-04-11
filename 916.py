# words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
# words2 = ["e", "o"]

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lc", "eo"]

from collections import defaultdict


def wordSubsets(words1, words2):
    status = False
    new_list = []
    words2_dict = defaultdict(int)
    words1_dict = defaultdict(int)

    for char in words2:
        for c in char:
            if c in words2_dict:
                words2_dict[c] += 1
            else:
                words2_dict[c] = 1

    for word in words1:
        for char in word:
            if char in words1_dict:
                words2_dict[char] += 1
            else:
                words2_dict[char] = 1

    for word in words1:
        for char in word:
            print(words1_dict)
            print(words2_dict)
            if words1_dict[char] == words2_dict[char]:
                status = True
            else:
                break
        if status:
            new_list.append(word)

    return new_list


wordSubsets(words1, words2)
