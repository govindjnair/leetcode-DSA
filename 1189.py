from collections import defaultdict


def maxNumberOfBalloons(text: str) -> int:
    word = "balloon"
    counter = defaultdict(int)
    for char in text:
        if char in word:
            counter[char] += 1

    if any(char not in counter for char in word):  # will return True if one value in the iterables is true
        return 0
    else:
        return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])


















# print(maxNumberOfBalloons("nllbblooon"))
# print(maxNumberOfBalloons("loonbalxballpoon"))
# print(maxNumberOfBalloons("nlaebolko"))
# print(maxNumberOfBalloons("leetcode"))
print(maxNumberOfBalloons("balllllllllllloooooooooon"))





