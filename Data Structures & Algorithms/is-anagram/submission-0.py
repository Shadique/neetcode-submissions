class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def make_dict(s):
            dict_ = {}
            for i in s:
                if i in dict_:
                    dict_[i] += 1
                else:
                    dict_[i] = 1
            return dict_

        dict1 = make_dict(s)
        dict2 = make_dict(t)
        
        if dict1 == dict2:
            return True
        else:
            return False