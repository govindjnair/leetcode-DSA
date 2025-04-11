def mergeAlternately(word1: str, word2: str) -> str:
    new_word = []
    A = len(word1)
    B = len(word2)
    a, b = 0, 0
    word = 1
    while a < A and b < B:
        if word == 1:
            new_word.append(word1[a])
            a += 1
            word = 2
        else:
            new_word.append(word2[b])
            b += 1
            word = 1

    while a < A:
        new_word.append(word1[a])
        a += 1

    while b < B:
        new_word.append(word2[b])
        b += 1

    return ''.join(new_word)

print(mergeAlternately(word1 ="cdf", word2="a"))