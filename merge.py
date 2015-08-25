# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        ans = []
        for itv in intervals:
            if not ans or ans[-1].end < itv.start:
                ans.append(itv)
            else:
                mergeItv = Interval(ans[-1].start,max(ans[-1].end,itv.end))
                ans[-1] = mergeItv
        return ans

a = Solution()
ans = a.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)])
for x in ans:
    print x.start,x.end