class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        l_max = height[l]
        r_max = height[r]
        res = 0
        while l < r:
            if l_max < r_max:
                res += l_max - height[l]
                l += 1
                l_max = max(height[l], l_max)
            else:
                res += r_max - height[r]
                r -= 1
                r_max = max(height[r], r_max)
        return res
