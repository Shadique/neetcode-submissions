class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # If un sorted part right
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
            if left == right:
                return nums[left]
        return 0
