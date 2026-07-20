class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def make_dict(n):
            dict_ = {}
            for i in n:
                if i in dict_:
                    dict_[i] += 1
                else:
                    dict_[i] = 1
            return dict_

        counter = make_dict(nums)
        return sorted(counter, key = counter.get, reverse = True)[:k]
        