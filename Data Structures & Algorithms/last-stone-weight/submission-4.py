class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minHeap = []

        for stone in stones:
            minHeap.append(-1 * stone)

        heapq.heapify(minHeap)

        while minHeap:
            if len(minHeap) == 1:
                break
            stone1 = heapq.heappop(minHeap)
            stone2 = heapq.heappop(minHeap)

            if stone1 == stone2:
                continue
            elif stone1 < stone2: # 10 > 5 ---> -10, -5 ---> -10 < -5
                stone1 -= stone2
                heapq.heappush(minHeap, stone1)
            else:
                stone2 -= stone1
                heapq.heappush(minHeap, stone2)
        

        return -1 * minHeap[0] if minHeap else 0
        