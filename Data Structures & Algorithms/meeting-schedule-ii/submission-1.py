"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x:x.start)

        pq = []

        for i in intervals:
            if pq and i.start >= pq[0]:
                heapq.heappop(pq)

            heapq.heappush(pq, i.end)

        return len(pq)



        