import re


def is_valid_string(s):
    # Regular expression to check if the string ends with numbers, no digits in between, and the first number is not '0'
    pattern = r'^[^\d]*[1-9]\d*$'
    return bool(re.match(pattern, s))
