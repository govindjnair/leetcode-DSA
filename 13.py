def romanToInt(s: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    new_num = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1:   # for some reason i < len(s) - 2 is more efficient
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                temp_num = roman_dict[s[i + 1]] - roman_dict[s[i]]
                new_num += temp_num
                i += 2
            else:
                new_num += roman_dict[s[i]]
                i += 1
        else:
            new_num += roman_dict[s[i]]
            i += 1

    return new_num


print(romanToInt("MCMXCIV"))
