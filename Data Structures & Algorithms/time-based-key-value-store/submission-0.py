class TimeMap:
    
    def __init__(self):
        self.st = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.st[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.st:
            return ""
        
        values = self.st[key]

        left = 0
        right = len(values)-1
        result = ""

        while left <= right:
            mid = (left+right)//2
            ts, val = values[mid]

            if ts <= timestamp:
                result = val
                left = mid+1
            else:
                right = mid-1

        return result
