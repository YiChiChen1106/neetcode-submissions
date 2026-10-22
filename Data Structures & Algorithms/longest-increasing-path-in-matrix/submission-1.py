class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        Rows,Cols = len(matrix),len(matrix[0])

        dp = [[0] * Cols for _ in range(Rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r,c):
            if dp[r][c] != 0:
                return dp[r][c]
            res = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < Rows and
                    0 <= nc < Cols and
                    matrix[nr][nc] > matrix[r][c]):

                    res = max(res, 1 + dfs(nr, nc))

            dp[r][c] = res
            return res
        
        res = 0
        for r in range(Rows):
            for c in range(Cols):
                res = max(res, dfs(r, c))
        
        return res

        