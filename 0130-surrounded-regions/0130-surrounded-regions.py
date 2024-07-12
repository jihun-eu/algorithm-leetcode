class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_row = len(board)
        max_col = len(board[0])
        if max_row < 3 or max_col < 3:
            return

        queue = []
        for row in range(max_row):
            if board[row][0] == "O":
                queue.append((row, 0))
            if board[row][max_col - 1] == "O":
                queue.append((row, max_col - 1))

        for col in range(max_col):
            if board[0][col] == "O":
                queue.append((0, col))
            if board[max_row - 1][col] == "O":
                queue.append((max_row - 1, col))

        while queue:
            row, col = queue.pop(0)
            board[row][col] = "#"

            for moved_row, moved_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if not ((0 <= moved_row < max_row) and (0 <= moved_col < max_col)):
                    continue
                if board[moved_row][moved_col] != "O":
                    continue
                queue.append((moved_row, moved_col))

        
        for row in range(max_row):
            for col in range(max_col):
                if board[row][col] == "#":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
        