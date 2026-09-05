class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)

                if value in rows[row]:
                    return False

                if value in cols[col]:
                    return False

                if value in boxes[box_index]:
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[box_index].add(value)

        return True
