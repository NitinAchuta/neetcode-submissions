class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        if key not in self.m:
            return res
        l, r = 0, len(self.m[key]) - 1


        while l <= r:
            # Get the list for the curr key 
            curr = self.m[key]
            mid = (r + l) // 2

            mVal = curr[mid][0]
            if mVal > timestamp:
                r = mid - 1
            elif mVal <= timestamp:
                res = curr[mid][1]
                l = mid + 1

        
        return res




        
