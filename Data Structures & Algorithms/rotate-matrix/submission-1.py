class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first row becomes last column
        # last row becomes first column
        #   4 6 7
        #   1 2 3
        #   9 6 5

        n = len(matrix)

        # Transpose: column index becomes row index
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col]
                )

        # Reverse every row
        for row in matrix:
            row.reverse()