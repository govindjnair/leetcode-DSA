def isValid(s: str) -> bool:
    stk = []
    closeAndOpen = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c not in closeAndOpen:
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != closeAndOpen[c]:
                    return False

    return not stk


# print(isValid("()[]{}"))
print(isValid("(]"))