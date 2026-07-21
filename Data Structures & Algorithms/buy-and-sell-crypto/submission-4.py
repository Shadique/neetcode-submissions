class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_buy = prices[0]
        for cur in prices:
            min_buy = min(min_buy, cur)
            result = max(result, cur - min_buy)
            
        return result
        