class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r={}
        c={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r[i]=0
                    c[j]=0

        for i in range(len(matrix)):
            if i in r:
                matrix[i]=[0]*len(matrix[0])
        
        for i in range(len(matrix[0])):
            if i in c:
                for j in range(len(matrix)):
                    matrix[j][i]=0    