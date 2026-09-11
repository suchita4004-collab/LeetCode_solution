```python id="x7k2m4"
class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, index):
            # All characters of the word are found
            if index == len(word):
                return True

            # Check boundaries and character match
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[index]):
                return False

            # Mark the current cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Explore four directions
            found = (
                backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1)
            )

            # Restore the cell
            board[row][col] = temp

            return found

        # Try every cell as the starting point
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True

        return False
```
