class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_res = 0
        n = len(prices)
        for i in range(n):
            cur_max_i = 0
            for j in range(i+1):
                cur_res = 0
                if prices[j] < prices[i]:
                    cur_res = prices[i] - prices[j]
                    #print(cur_res, prices[j], prices[i])
                cur_max_i = max(cur_max_i, cur_res)
                #print(cur_res, cur_max_i, prices[i], prices[j])
            max_res = max(max_res, cur_max_i)
        return max_res