import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minHeap = [(0, 0)]   # (cost, node)
        visited = set()

        res = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)

            # 已经加入 MST，跳过
            if i in visited:
                continue

            # 把这个点加入 MST
            visited.add(i)
            res += cost

            x1, y1 = points[i]

            # 计算它到所有未访问节点的距离
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]

                    dist = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(minHeap, (dist, j))

        return res