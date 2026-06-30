class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
          seen = set()
          for j in range(len(board)):
            if board[i][j] != "." and int(board[i][j])>9:
                return False
            if board[i][j] == ".":
                continue
            if board[i][j] in seen:
                return False
            seen.add(board[i][j])

        for j in range(len(board)):
            seen = set()
            for i in range(len(board)):
              if board[i][j] != "." and int(board[i][j])>9:
                return False
              if board[i][j] == ".":
                continue
              if board[i][j] in seen:
                return False 
              seen.add(board[i][j])

        for row in range(0,len(board),3):
            for col in range(0,len(board),3):
               seen = set()
               for i in range(row,row+3):
                 for j in range(col,col+3):
                    if board[i][j] == ".":
                      continue
                    if board[i][j] in seen:
                      return False
                    seen.add(board[i][j])

        return True                                     