class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        dict_ = dict()
        for i in range(l):
            lower = target - nums[i]
            if lower in dict_:
                return [dict_[lower], i]
            else:
                dict_[nums[i]] = i
        return [0,0]
