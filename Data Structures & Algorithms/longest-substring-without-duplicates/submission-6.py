class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        n = len(s)
        if n == 0 or n == 1:
            return n
        res = 0
        l = 0
        r = 0
        cur = 0
        while r < n:
            if s[r] in set_:
                res = max(res, cur)
                set_.remove(s[l])
                l += 1
                cur -= 1
                
            else:
                cur += 1
                set_.add(s[r])
                r += 1
        return max(res, cur)
