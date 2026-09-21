class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_hash = {}
        freq = [[]for i in range(len(nums) + 1)]

        for element in nums:
            my_hash[element] = 1 + my_hash.get(element, 0)
        for n, v in my_hash.items():
            freq[v].append(n)

        res =[]
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res

