class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        VISITED = '.'
        move = [0,1,0,-1,0]
        
        def dfs(row: int, col: int, idx: int) -> bool:
            nonlocal board, word, move, VISITED

            if len(word) == idx:
                return True

            if not(0 <= row < len(board) and 0 <= col < len(board[0])):
                return False

            if board[row][col] != word[idx] or board[row][col] == VISITED:
                return False
            
            tmp = board[row][col]
            
            board[row][col] = VISITED
            nextIdx = idx + 1
            if dfs(row+1, col, nextIdx) or dfs(row-1, col, nextIdx) or dfs(row, col+1, nextIdx) or dfs(row, col-1, nextIdx):
                return True

            board[row][col] = tmp

            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        
        return False