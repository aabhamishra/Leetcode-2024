class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # to check for duplicate numbers in each row and in 3x3 sub-boxes
        unique = set()
        box_map = {}

        for row in range(9):
            unique = set()
            for col in range(9):
                # this ensures that numbers in the same sub-box map to the same key in box_map
                i = row // 3
                j = col // 3
                box_set = box_map.get((i, j), set())

                if board[row][col].isdigit():
                    if board[row][col] in box_set:
                        return False
                    if board[row][col] in unique:
                        return False
                box_set.add(board[row][col])
                box_map[(i, j)] = box_set
                unique.add(board[row][col])
        
        # to check for duplicate numbers in each column
        for col in range(9):
            unique = set()
            for row in range(9):
                if board[row][col].isdigit() and board[row][col] in unique:
                    return False
                unique.add(board[row][col])
        
        return True



        

