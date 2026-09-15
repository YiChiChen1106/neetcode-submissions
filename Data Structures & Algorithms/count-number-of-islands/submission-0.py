class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= Rows or c < 0 or c >= Cols or grid[r][c] == "0": 
                return
            grid[r][c] = "0"
            dfs(r,c + 1)
            dfs(r,c - 1)
            dfs(r + 1,c)
            dfs(r - 1,c)
        
        islands = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands