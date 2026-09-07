class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # Check rows
        for row in range(rows):
            rowSet = set()

            for col in range(cols):
                value = board[row][col]

                if value == ".":
                    continue

                if value in rowSet:
                    return False

                rowSet.add(value)

        # Check columns
        for col in range(cols):
            colSet = set()

            for row in range(rows):
                value = board[row][col]

                if value == ".":
                    continue

                if value in colSet:
                    return False

                colSet.add(value)

        # Check each 3x3 square
        for starting_row in range(0, rows, 3):
            for starting_col in range(0, cols, 3):
                sqSet = set()

                for row in range(starting_row, starting_row + 3):
                    for col in range(starting_col, starting_col + 3):
                        value = board[row][col]

                        if value == ".":
                            continue

                        if value in sqSet:
                            return False

                        sqSet.add(value)

        return True