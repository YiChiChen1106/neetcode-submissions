class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    row_key = f"{val} in row{i}"
                    col_key = f"{val} in col{j}"
                    box_key = f"{val} in box{i//3}-{j//3}"
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
    
        return True
        