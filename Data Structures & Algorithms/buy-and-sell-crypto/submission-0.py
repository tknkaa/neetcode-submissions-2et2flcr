class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = [0] * len(prices)
        i = 0
        while i < len(prices):
            if i == 0:
                prefix[i] = prices[i]
            else:
                prefix[i] = min(prefix[i - 1], prices[i])
            i += 1
        suffix = [0] * len(prices)
        i = len(prices) - 1
        while i >= 0:
            if i == len(prices) - 1:
                suffix[i] = prices[i]
            else:
                suffix[i] = max(suffix[i - 1], prices[i])
            i -= 1
        profits = [0] * len(prices)
        while i < len(prices):
            profits[i] = suffix[i] - prefix[i]
            i += 1
        return max(profits)
        