class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for i in range(9):
                if row[i] in s:
                    return False
                else:
                    if row[i] != ".":
                        s.add(row[i])
                
        
        i = j = 0
        while(j < 9):
            s = set()
            i = 0
            while(i < 9):
                cur = board[i][j]
                if cur in s:
                    return False
                else:
                    if cur != ".":
                        s.add(cur)
            
                i += 1
            j += 1
        sqi = 0
        while sqi < 9:
            sqj = 0
            while sqj < 9:
                s = set()
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        cur = board[sqi + i][sqj + j]
                        if cur in s:
                            return False
                        else:
                            if cur != ".":
                                s.add(cur)
                        j += 1
                    i += 1
                sqj += 3
            sqi += 3
            
        

        return True