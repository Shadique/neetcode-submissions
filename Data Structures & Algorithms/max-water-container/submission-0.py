class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_result = 0
        i = 0 
        j = len(heights) - 1
        while i < j:
            cur_area = min(heights[i], heights[j]) * (j - i)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            max_result = max(max_result, cur_area)
        return max_result