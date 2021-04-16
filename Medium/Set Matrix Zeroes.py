class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        
        cols = set()
        rows = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        
        for i in rows:
            matrix[i] = [0]*len(matrix[i])
        
        for i in range(len(matrix)):
            if i in rows:
                continue
            for j in cols:
                matrix[i][j] = 0
        
        return matrix