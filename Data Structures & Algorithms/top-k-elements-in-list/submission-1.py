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
        l = len(nums)
        freq_arr = [set() for _ in range(l)]
        for i in nums:
            freq_arr[counter[i] - 1].add(i)
        result = []
        for i in range(l - 1, -1, -1):
            cur = freq_arr[i]
            if cur:
                result = result + list(cur)

        return result[:k]