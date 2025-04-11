# words = ["a", "aba", "ababa", "aa"]
# words = ["pa", "papa", "ma", "mama"]


# words = ["abab","ab"]
# words = ["a","abb"]
words = ["bc", "b", "ab"]


def countPrefixSuffixPairs(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # check both prefix and suffix
            if words[i] in words[j][:len(words[i])] and words[i][::-1] in words[j][::-1][:len(words[i])]:
                count += 1
                print(words[i], words[j])
    print(count)


countPrefixSuffixPairs(words)
