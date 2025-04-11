def maxProfit(prices: list[int]) -> int:
    # time O(n)
    # space O(1)

    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit






print(maxProfit(prices = [3,2,6,5,0,3]))