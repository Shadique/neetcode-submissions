class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_buy = prices[0]
        n = len(prices)
        for cur in prices:
            if min_buy > cur:
                min_buy = cur
            result = max(result, cur - min_buy)

        
        return result
        