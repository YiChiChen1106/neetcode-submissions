class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        rowZero = False
        colZero = False

        for c in range(COLS):
            if matrix[0][c] == 0:
                rowZero = True
        
        for r in range(ROWS):
            if matrix[r][0] == 0:
                colZero = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if colZero:
            for r in range(ROWS):
                matrix[r][0] = 0
        



        
        