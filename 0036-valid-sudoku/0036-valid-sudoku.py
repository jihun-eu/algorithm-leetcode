class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            tmp = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in tmp:
                    return False
                tmp.add(board[i][j])

        for j in range(len(board)):
            tmp = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in tmp:
                    return False
                tmp.add(board[i][j])
                 
        
        for row in range(0,len(board),3):
            for col in range(0,len(board),3):
                tmp = set()
                for i in range(3):
                    for j in range(3):
                        currRow, currCol = row+i, col+j
                        if board[currRow][currCol] == '.':
                            continue
                        if board[currRow][currCol] in tmp:
                            return False
                        tmp.add(board[currRow][currCol])
        return True

