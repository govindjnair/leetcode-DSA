def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = ["+", "-", "*", "/"]

    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            pop1 = stack.pop()
            pop2 = stack.pop()
            if token == "+":
                stack.append(int(pop2) + int(pop1))
            elif token == "-":
                stack.append(int(pop2) - int(pop1))
            elif token == "*":
                stack.append(int(pop2) * int(pop1))
            else:
                stack.append(int(pop2) / int(pop1))



    return int(stack.pop())

print(evalRPN(["4","13","5","/","+"]))