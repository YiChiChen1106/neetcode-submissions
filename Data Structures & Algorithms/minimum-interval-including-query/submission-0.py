
import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()

        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        res = [-1] * len(queries)
        heap = []
        i = 0

        for q, index in sorted_queries:

            # 1. Add all intervals whose left <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                length = r - l + 1
                heapq.heappush(heap, (length, r))
                i += 1

            # 2. Remove intervals that cannot cover q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # 3. Get the shortest valid interval
            if heap:
                res[index] = heap[0][0]

        return res
