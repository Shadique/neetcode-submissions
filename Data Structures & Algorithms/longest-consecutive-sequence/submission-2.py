# 1 2 3 4 8 9 10 11 12

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        nums.sort()
        result = [nums[0]]
        cur = [nums[0]]
        for i in range(1, len(nums)):
            cur_last = cur[len(cur) - 1]
            if nums[i] ==  cur_last + 1:
                cur.append(nums[i])
            elif nums[i] == cur_last:
                pass
            else:
                cur = [nums[i]]
            if len(result) < len(cur):
                result = cur
            
        return len(result)

