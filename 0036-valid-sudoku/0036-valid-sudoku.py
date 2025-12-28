class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=[set() for row in range(9)]
        cols=[set() for col in range(9)]
        box = {}

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == "." :
                    continue
                if cell in rows[row]:
                    return False
                rows[row].add(cell)
                if cell in cols[col]:
                    return False
                cols[col].add(cell)

                box_index = (row//3,col//3)

                if box_index not in box:
                    box[box_index]=set()
                if cell in box[box_index]:
                    return False
                box[box_index].add(cell)
        return True
                



                

        