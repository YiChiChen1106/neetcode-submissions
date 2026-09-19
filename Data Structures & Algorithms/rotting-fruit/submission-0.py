from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        q = deque()
        fresh = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]        
        minutes =  0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nc < Cols and 0 <= nr < Rows and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1
        
        if fresh == 0:
            return minutes
        
        return -1



            


        