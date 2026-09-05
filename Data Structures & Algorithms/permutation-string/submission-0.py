class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def counter(s):
            freq = {}
            for i in s:
                freq[i] = 1 + freq.get(i, 0)
            return freq
            
        freq1 = counter(s1)
        l = len(s1)
        freq2 = counter(s2[:l])
        if freq1 == freq2:
            return True
        i = 0
        while l < len(s2):
            freq2[s2[l]] = 1 + freq2.get(s2[l], 0)
            l += 1
            print(s2[i], freq2)
            freq2[s2[i]] -=  1
            if freq2[s2[i]] == 0:
                freq2.pop(s2[i])
            if freq1 == freq2:
                return True
            i += 1

        return False