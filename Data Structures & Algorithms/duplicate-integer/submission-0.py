class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for i in nums:
            if i in set_:
                return True
            else:
                set_.add(i)
        return False