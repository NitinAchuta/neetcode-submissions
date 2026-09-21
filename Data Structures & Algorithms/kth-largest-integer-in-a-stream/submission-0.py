class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.numss = nums
        

    def add(self, val: int) -> int:
        self.numss.append(val)
        temp = sorted(self.numss)
        return temp[len(self.numss) - self.kth]
        
