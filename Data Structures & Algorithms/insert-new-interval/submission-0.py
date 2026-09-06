class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0

        # Find where newInterval should be inserted
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        intervals.insert(i, newInterval)

        # Merge intervals
        res = []

        for curr in intervals:
            if not res:
                res.append(curr)
            else:
                prev = res[-1]

                if curr[0] <= prev[1]:
                    prev[1] = max(prev[1], curr[1])
                else:
                    res.append(curr)

        return res