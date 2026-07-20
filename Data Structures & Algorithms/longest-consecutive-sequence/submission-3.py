# 1 2 3 4 8 9 10 11 12

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        s = set(nums)
        
        result = 0
        for i in s:
            if  i - 1 not in s:
                cur = 1
                while (i + cur) in s:
                    cur += 1
                result = max(result, cur)
        return result
