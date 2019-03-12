"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
Time: O(N*M)
Sapce: O(N*M)
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                if self.traverse_board(0, board, row, col, word):
                    return True
        return False
    def traverse_board(self, char_index, board, row, col, word):
        if char_index == len(word):
            return True
        if 0 <= row < len(board) and 0 <= col <len(board[0]) and board[row][col]==word[char_index]: 
            temp, board[row][col] = board[row][col], '#'
            direction = ((1,0),(-1,0),(0,1),(0,-1))
            for x, y in direction:
                if self.traverse_board(char_index+1, board, row+x, col+y, word): 
                    return True
            board[row][col] = temp
        return False