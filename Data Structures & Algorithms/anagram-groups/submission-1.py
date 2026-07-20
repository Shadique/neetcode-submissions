class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def make_dict(s):
            dict_ = {}
            for i in s:
                if i in dict_:
                    dict_[i] += 1
                else:
                    dict_[i] = 1
            return dict_
        def is_anagram(d1, d2):
            return d1 == d2
        
        l = len(strs)
        result = []
        used = set()
        for i in range(l):
            if i in used:
                continue
            cur = [strs[i]]
            used.add(i)
            di = make_dict(strs[i])
            for j in range(i+1, l):
                if j in used:
                    continue
                dj = make_dict(strs[j])
                if is_anagram(di, dj):
                    cur.append(strs[j])
                    used.add(j)
            result.append(cur)
        return result

