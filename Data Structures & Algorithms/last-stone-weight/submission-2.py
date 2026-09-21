import heapq # Maximum heap as we will be using the heaviest stones everytime

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            
            if first != second:
                heapq.heappush(maxHeap, first - second)

        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0]

        
        