# p  1 , 1,  2, 8
# r  1 , 2 , 4, 6
# s 48, 24 , 6, 1


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1]
        cur_p = 1
        for i in range(l - 1):
            cur_p *= nums[i]
            pre.append(cur_p)
        
        suf = [1]*l
        cur_p = 1
        for i in range(l-1, 0, -1):
            cur_p *= nums[i]
            suf[i - 1] = cur_p
        result = [1] * l
        for i in range(l):
            result[i] = pre[i] * suf[i]
        return result