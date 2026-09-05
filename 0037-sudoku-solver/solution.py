class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    empty.append((row, col))
                else:
                    rows[row].add(value)
                    cols[col].add(value)

                    box = (row // 3) * 3 + (col // 3)
                    boxes[box].add(value)

        def backtrack(index):
            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row // 3) * 3 + (col // 3)

            for num in "123456789":
                if num in rows[row] or num in cols[col] or num in boxes[box]:
                    continue

                board[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)

                if backtrack(index + 1):
                    return True

                board[row][col] = "."
                rows[row].remove(num)
                cols[col].remove(num)
                boxes[box].remove(num)

            return False

        backtrack(0)
