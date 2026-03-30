class Solution:
    def isValidSudoku(self, board):

        # Check rows
        for row in board:
            nums = [x for x in row if x != "."]
            if len(nums) != len(set(nums)):
                return False

        # Check columns
        for col in range(9):
            nums = []
            for row in range(9):
                if board[row][col] != ".":
                    nums.append(board[row][col])
            if len(nums) != len(set(nums)):
                return False

        # Check 3x3 boxes
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_row+i][box_col+j]
                        if val != ".":
                            nums.append(val)

                if len(nums) != len(set(nums)):
                    return False

        return True
