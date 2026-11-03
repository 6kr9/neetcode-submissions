class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        print(intervals)
        ans = 0
        end = float('-inf')
        
        for s,f in (intervals):

            if s >= end:
                end = f         
            else:
                ans += 1

        return ans    
        