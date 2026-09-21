class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows = len(board)
        Cols = len(board[0])
        def dfs(r,c):
            if ( r < 0 or r >= Rows or c < 0 or c >= Cols
            or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfs(r - 1,c)
            dfs(r + 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
        
        for r in range(Rows):
            dfs(r,0)
            dfs(r,Cols - 1)
        
        for c in range(Cols):
            dfs(0,c)
            dfs(Rows - 1,c)
        
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

        