"""
Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.
Time: O(NlogN)
Space: O(N)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key = lambda x: x.start)
        endpoint = intervals[0].end
        overlap = 0
        for i in range(1,len(intervals)):
            if endpoint > intervals[i].start:
                overlap += 1
                endpoint = min(endpoint,intervals[i].end)
            else:
                endpoint = intervals[i].end
        return overlap