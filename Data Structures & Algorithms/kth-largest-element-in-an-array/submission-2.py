class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-1*num for num in nums]
        heapq.heapify(maxHeap)
        # print(maxHeap, k)

        res = None
        for i in range(k):
            res = heapq.heappop(maxHeap)
            # print(res)
        
        return res * -1
        