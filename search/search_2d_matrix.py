class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, col = 0, len(matrix[0]) - 1 # the trick is to start from top right corner
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # since all numbers along this row are non-decreasing
                # this means that all the numbers before col index in the same row are smaller
                # so we eliminate this row
                row += 1
            else: # matrix[row][col] > target
                # since all numbers along this column are non-decreasing
                # this means that all numbers after this row in the same column are bigger
                # so we eliminate this column
                col -= 1
        return False
