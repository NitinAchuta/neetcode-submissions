class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.numss = nums
        

    def add(self, val: int) -> int:
        self.numss.append(val)
        self.numss.sort()
        return self.numss[len(self.numss) - self.kth]
        
