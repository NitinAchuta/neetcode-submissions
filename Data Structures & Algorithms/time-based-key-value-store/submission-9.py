class TimeMap:

    def __init__(self):
        self.myDict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict[key] = [(timestamp, value)]
        else:
            self.myDict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.myDict:
            return ""

        l = 0
        r = len(self.myDict[key]) - 1
        res, values = "", self.myDict.get(key, [])
        while l <= r:

            m = (l + r ) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        
