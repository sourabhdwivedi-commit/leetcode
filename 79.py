class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        if board.count(word[0])>board.count(word[-1]):
            word=word[::-1]
        def dfs(i,j,t):
            if t==len(word):
                return True
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!=word[t]:
                return False
            temp=board[i][j]
            board[i][j]='#'
            found=dfs(i+1,j,t+1) or dfs(i-1,j,t+1) or dfs(i,j+1,t+1) or dfs(i,j-1,t+1)
            board[i][j]=temp
            return found 

 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True


        return False           

        