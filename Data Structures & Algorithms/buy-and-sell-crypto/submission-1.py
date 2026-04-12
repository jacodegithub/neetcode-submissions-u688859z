class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        while i < j and j < len(prices):
            profit = prices[j] - prices[i]
            if profit <= 0:
                i = j
                j += 1
            elif profit > 0:
                j += 1
            max_profit = max(max_profit, profit)
        return max_profit

        