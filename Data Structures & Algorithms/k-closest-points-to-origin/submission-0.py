import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        # maxHeap that stores all distances
        # Hash that stores distance -> point

        # while constructing maxHeap
            # if new point < maxHeap[0]
                # pop maxHeap, append
            # otherwise keep moving

        # res list
        # for distances in minHeap
        #res.append(hash[distance])

        maxHeap = []

        for point in points:
            currD = -1 * math.sqrt(point[0]**2 + point[1]**2)

            heapq.heappush(maxHeap, (currD, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = [[point[1][0], point[1][1]] for point in maxHeap]
        return res
        

        