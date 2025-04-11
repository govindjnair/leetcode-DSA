# fibonacci number
# naive approach recursion

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(6))

# top down DP / Memoization

def fibo(n: int) -> int:
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x - 1) + f(x - 2)
            return memo[x]

    return f(n)


# print(fibo(6))

# bottom up approach


def fibona(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# print(fibona(6))

# without using list

def fibonac(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1

    for i in range(2, n + 1):
        prev, curr = curr, prev+curr

    return curr

print(fibonac(6))