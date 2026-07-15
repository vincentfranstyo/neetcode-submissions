class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row 1 - 9 no duplicates
        # check column 1 - 9 no duplicates
        col = defaultdict(list[int])
        boxes = defaultdict(list[int])
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    boxes[(i // 3 * 3) + (j // 3)].append(board[i][j])
                    row.append(board[i][j])
                    col[j].append(board[i][j])
            
                if len(set(row)) != len(row):
                    return False

        for i in range(9):
            if len(set(col[i])) != len(col[i]):
                return False
            
            if len(set(boxes[i])) != len(boxes[i]):
                return False

        return True
                
                

                
                