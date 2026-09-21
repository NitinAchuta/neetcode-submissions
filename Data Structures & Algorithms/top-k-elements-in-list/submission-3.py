import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {}

        for num in nums:
            myDict[num] = 1 + myDict.get(num, 0)
        
        myHeap = []
        for num in myDict.keys():
            heapq.heappush(myHeap, (myDict[num], num))
            if len(myHeap) > k:
                heapq.heappop(myHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(myHeap)[1])

        return res

        