

-4, -1, -1, 0, 1, 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        l = len(nums)
        for i in range(l):
            set_ = set()
            target = nums[i]
            for j in range(i + 1, l):
                sub = -(target + nums[j])
                # print("set = ", set_)
                # print(sub, target, nums[j])
                if sub in set_:
                    cur_result = tuple(sorted([sub,target,nums[j]]))
                    result.add(cur_result)
            
                set_.add(nums[j])
        #print(result)
        return [list(i) for i in result]
                    