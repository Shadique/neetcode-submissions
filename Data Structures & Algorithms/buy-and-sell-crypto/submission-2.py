class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i = 0 
        j = 1
        n = len(prices)
        while i < n and j < n:
            if prices[i] >= prices[j]:
                i = j
                j+= 1
            else:
                result = max(result, prices[j] - prices[i])
                j += 1

        return result
        