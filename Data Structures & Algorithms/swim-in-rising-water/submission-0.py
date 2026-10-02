import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                ):
                    newTime = max(time, grid[nr][nc])

                    heapq.heappush(
                        minHeap,
                        (newTime, nr, nc)
                    )