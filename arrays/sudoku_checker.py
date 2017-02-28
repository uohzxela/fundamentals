import math

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.hasValidRows(board) and
                self.hasValidCols(board) and
                self.hasValidSubgrids(board))
    
    def hasValidRows(self, board):
        for i in xrange(len(board)):
            if self.hasDuplicate(board, i, i+1, 0, len(board[0])):
                return False
        return True
    
    def hasValidCols(self, board):
        for i in xrange(len(board[0])):
            if self.hasDuplicate(board, 0, len(board), i, i+1):
                return False
        return True
    
    def hasValidSubgrids(self, board):
        regionSize = int(math.sqrt(len(board)))
    	for i in xrange(regionSize):
    		for j in xrange(regionSize):
    			if self.hasDuplicate(board, regionSize*i, regionSize*(i+1), 
    			                     regionSize*j, regionSize*(j+1)):
    				return False
    	return True
    	
    def hasDuplicate(self, board, srow, erow, scol, ecol):
        found = set()
        for i in xrange(srow, erow):
            for j in xrange(scol, ecol):
                num = board[i][j]
                if num == '.':
                    continue
                if num in found:
                    return True
                found.add(num)
        return False
