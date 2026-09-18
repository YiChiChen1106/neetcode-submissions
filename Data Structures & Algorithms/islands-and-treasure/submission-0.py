class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows = len(grid)
        Cols = len(grid[0])
        q = deque()

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(-1,0),
                        (1,0),
                        (0,-1),
                        (0,1)]

        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= Rows or nc < 0 or nc >= Cols:
                    continue
                
                if grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc))









        