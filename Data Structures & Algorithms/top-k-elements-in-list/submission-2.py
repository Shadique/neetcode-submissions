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
        freq_arr = [[] for _ in range(l+1)]
        for num, freq in counter.items():
            freq_arr[freq].append(num)
        result = []
        print(freq_arr)
        for i in range(l, 0, -1):
            cur = freq_arr[i]
            if cur:
                result = result + cur

        return result[:k]