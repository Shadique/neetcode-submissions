

-4, -1, -1, 0, 1, 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        result = set()
        for i in range(l):
            target = nums[i]
            j = i + 1
            k = l - 1
            while j < k:
                if target == -(nums[j] + nums[k]):
                    cur_result = tuple(sorted([target, nums[j], nums[k]]))
                    result.add(cur_result)
                    j += 1
                    k -= 1
                    continue
                elif target < -(nums[j] + nums[k]):
                    j += 1
                else:
                    k -= 1
        return [list(i) for i in result]
                    