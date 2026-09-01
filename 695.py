class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>= rows or c>=cols or grid[r][c]==0:
                return 0

            grid[r][c]=0
            return 1+ dfs(r+1,c) +dfs(r,c+1)+ dfs(r-1,c)+ dfs(r,c-1)

        ans=0
        for m in range(rows):
            for n in range(cols):
                if grid[m][n]==1:
                    ans=max(ans,dfs(m,n))

        return ans               