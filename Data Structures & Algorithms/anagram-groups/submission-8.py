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
        
        result = dict()
        for i in strs:
            cur_d = frozenset(make_dict(i).items())
            if cur_d in result:
                result[cur_d].append(i)
            else:
                result[cur_d] = [i]
        return list(result.values())