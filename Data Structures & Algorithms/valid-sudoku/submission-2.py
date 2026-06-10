class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows : List[set] = [set() for _ in range(9)]
        column : List[set] = [set() for _ in range(9)]
        boxes : List[List[set]] = [([set() for _ in range(3)]) for _ in range(3) ]
        
        for r in range(9):
            for c in range(9):
                number = board[r][c]
                if number == ".":
                    continue 

                if number not in rows[r]:
                    rows[r].add(number)
                else:
                    return False

                if number not in column[c]:
                    column[c].add(number)
                else:
                    return False

                ro = r //3
                co = c //3

                if number not in boxes[ro][co]:
                    boxes[ro][co].add(number)
                else:
                    return False

        return True

                