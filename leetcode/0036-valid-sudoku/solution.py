class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[i][j] 
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])
        s = [(0,0),(0,3),(0,6),
              (3,0),(3,3),(3,6),
              (6,0),(6,3),(6,6)]
        for i,j in (s):
            seen = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    if board[row][col] in seen:
                        return False
                    elif board[row][col] != '.':
                        seen.add(board[row][col])
        return True
                
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
