class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix=[]
        ROWS=len(matrix)
        COLS=len(matrix[0])
        for i in range(ROWS+1):
            row=[0]*(COLS+1)
            self.sumMatrix.append(row)
        
        for r in range(ROWS):
            prefix=0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1=row1+1
        col1=col1+1
        row2=row2+1
        col2=col2+1

        bottomright=self.sumMatrix[row2][col2]
        above=self.sumMatrix[row1-1][col2]
        left=self.sumMatrix[row2][col1-1]
        topleft=self.sumMatrix[row1-1][col1-1]
        return bottomright-above-left+topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)