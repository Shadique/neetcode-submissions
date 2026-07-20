class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        for i in range(n):
            buy = prices[i]
            for j in range(i+1, n):
                sell = prices[j]
                result = max(result, sell - buy)
        return result
        