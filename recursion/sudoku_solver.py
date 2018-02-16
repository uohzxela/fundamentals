class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def solve(self, board):
        r, c = self.find_unassigned_cell(board)
        if r == -1 and c == -1:
            return True
        
        for num in xrange(1, 10):
            if self.is_valid(board, r, c, str(num)):
                board[r][c] = str(num)
                if self.solve(board):
                    return True
                board[r][c] = '.'
        return False
    
    def find_unassigned_cell(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.':
                    return i, j
        return -1, -1
    
    def is_valid(self, board, r, c, num):
        return (self.is_valid_by_row(board, r, num) and
                self.is_valid_by_col(board, c, num) and
                self.is_valid_by_grid(board, r - r % 3, c - c % 3, num))
    
    def is_valid_by_row(self, board, r, num):
        return not (num in board[r])
    
    def is_valid_by_col(self, board, c, num):
        for i in xrange(len(board)):
            if board[i][c] == num:
                return False
        return True
    
    def is_valid_by_grid(self, board, r, c, num):
        for i in xrange(3):
            for j in xrange(3):
                if board[r + i][c + j] == num:
                    return False
        return True
