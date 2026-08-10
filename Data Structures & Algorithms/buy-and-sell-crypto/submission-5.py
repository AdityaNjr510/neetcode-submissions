class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        l, r = 0, 1
        minBuy = prices[l]

        while r < len(prices):
            maxProfit = max(prices[r] - minBuy, maxProfit)
            minBuy = min(prices[r], minBuy)
            r += 1

        return maxProfit