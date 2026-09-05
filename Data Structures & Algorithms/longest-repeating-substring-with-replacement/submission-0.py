class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}

        maxc = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxc = max(maxc, count[s[r]])

            if (r - l + 1) - maxc > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
