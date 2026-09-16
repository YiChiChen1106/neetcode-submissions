class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        def dfs(r,c):
            if (r < 0  or r >= Rows or c < 0 or c >= Cols or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            ans = 1 + dfs(r + 1,c) + dfs(r - 1,c) + dfs(r,c + 1) +dfs(r,c - 1)
            return ans
        
        area = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    area = max(area,dfs(r,c))
        
        return area
        


        