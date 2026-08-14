class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        cur_max = nums[0]
        result = nums[0]
        for i in range(1, l):
            cur_max = max(nums[i], nums[i] + cur_max)
            result = max(result , cur_max)
        return result