class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows(arr):
            for row in range(0, 9):
                ray = []
                for col in range(0, 9):
                    if board[row][col].isdigit():
                        ray.append(board[row][col])
                        if (len(ray) != len(set(ray))):
                            return False
            return True    
        def check_cols(arr):
            for col in range(0, 9):
                ray = []
                for row in range(0, 9):
                    if board[row][col].isdigit():
                        ray.append(board[row][col])
                        if (len(ray) != len(set(ray))):
                            return False
            return True      
        def check_boxes(arr):
            for start_row in range(0, 9, 3):
                for start_col in range(0, 9, 3):
                    hashmap = set()
                    for row in range(start_row, start_row + 3):
                        for col in range(start_col, start_col + 3):
                            if board[row][col].isdigit() and board[row][col] in hashmap:
                                return False
                            hashmap.add(board[row][col])
            return True

        return check_rows(board) & check_cols(board) & check_boxes(board)
        