class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = len(strs)
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
        arry_dict = [make_dict(i) for i in strs]
        
        result = []
        visited = set()
        for i in range(l):
            if i in visited:
                continue
            visited.add(i)
            cur = [strs[i]]
            for j in range(i+1, l):
                if j in visited:
                    continue
                if is_anagram(arry_dict[i], arry_dict[j]):
                    cur.append(strs[j])
                    visited.add(j)
            result.append(cur)
        return result