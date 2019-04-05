"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0

Time: O(m*n)
Space: O(1)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    
        def replace(zer_row,zer_col):
            for row in range(len(matrix)):
                if matrix[row][zer_col] != 0:
                    matrix[row][zer_col] = "#"
            for col in range(len(matrix[zer_row])):
                if matrix[zer_row][col] != 0:
                    matrix[zer_row][col] = "#"
                    
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    replace(row,col)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == "#":
                    matrix[row][col] = 0