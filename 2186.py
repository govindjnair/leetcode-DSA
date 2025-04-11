# s = "leetcode"
# t = "coats"

#
# s ="night"
# t = "thing"

# s = "cotxazilut"
# t = "nahrrmcchxwrieqqdwdpneitkxgnt"

# s = "nxkhahxvqy"
# t = "nbhqyoxwnx"

# s = "uxfgkiykldv"
# t = "ucyhpacdgmughvjtrmgf"

s = "rxzpxzawbcgwwrqaaiqwaeapjssnfexwxnphueulbfdmqvf"
t = "tzqkkgzfwxxkbrsfnibgqzqkuluoyiothgcmlncmmezclxpjralrdcpqvxtiqlvteu"


def minstepsanagram(s, t):
    count = 0
    counter_s = {}
    counter_t = {}
    for char in s:
        if char in counter_s:
            counter_s[char] += 1
        else:
            counter_s[char] = 1
    for char in t:
        if char in counter_t:
            counter_t[char] += 1
        else:
            counter_t[char] = 1

    all_chars = set(s + t)
    print(counter_s)
    print(counter_t)
    print(all_chars)
    for char in all_chars:
        count_s = counter_s.get(char, 0)
        count_t = counter_t.get(char, 0)
        count += abs(count_s-count_t)
    print(count)
    return count

print(minstepsanagram(s, t))
