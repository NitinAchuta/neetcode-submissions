import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {}
        for index, value in enumerate(nums): #Tuple of count, value
            myDict[value] = (1 + myDict.get(value, (0, value))[0], value)

        myHeap = []
        for key in myDict.keys():
            heapq.heappush(myHeap, myDict[key])
            if len(myHeap) > k:
                heapq.heappop(myHeap)

        res = []
        for val in myHeap:
            res.append(val[1])

        return res