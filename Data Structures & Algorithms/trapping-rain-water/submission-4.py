class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
            
        result = 0
        left_max = [height[0]]
        for i in range(1, l):
            left_max.append(max(left_max[i-1], height[i]))

        right_max = [0] * l
        right_max[l-1] = height[l-1]
        for i in range(l - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(l):
            result += min(left_max[i], right_max[i]) - height[i]
        return result