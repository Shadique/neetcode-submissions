class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
        result = 0
        for i in range(l):
            left_max = right_max = height[i]
            for j in range(i):
                left_max = max(left_max, height[j])
            for k in range(i+1, l):
                right_max = max(right_max, height[k])

            result += min(left_max, right_max) - height[i]
        return result