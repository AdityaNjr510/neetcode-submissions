class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(9):
            seen = set()
            for j in range(9):             
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        for i in range(9):
            seen = set()
            for j in range(9):   
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])

        for i in range(3):
            for j in range(3):
                seen = set()
                for m in range(i*3,i*3+3):
                    for n in range(j*3,j*3+3):
                        if board[m][n] != '.':
                            if board[m][n] in seen:
                                return False
                            else:
                                seen.add(board[m][n])

        return True



                

                    


            
