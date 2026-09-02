class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first row becomes last column
        # last row becomes first column
        #   4 6 7
        #   1 2 3
        #   9 6 5

        temp = 0
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        for i in range(len(matrix)//2):
            for j in range(len(matrix[0])):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[rows-i][j]
                matrix[rows-i][j] = temp
        
        
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]