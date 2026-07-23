class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        n = len(s)
        if n == 0:
            return 0
        res = 1
        for i in range(n):
            set_ = set(s[i])
            cur = 1
            for j in range(i+1, n):
                if s[j] in set_:
                    res = max(res, cur)
                    break
                else:
                    set_.add(s[j])
                    cur += 1
            res = max(res, cur)
        return res