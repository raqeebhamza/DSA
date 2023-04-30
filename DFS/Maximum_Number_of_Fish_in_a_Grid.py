class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        
        res=0
        n=len(grid)
        m=len(grid[0])
        visited=set()
        
        def dfs(i,j):
            nonlocal res
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            curr = 0
            for r,c in ((0,1),(0,-1),(1,0),(-1,0)):
                if 0 <= i + r < n and 0 <= j + c < m:
                    curr+=dfs(i+r, j+c)
            return curr+grid[i][j]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    if (i,j) not in visited:
                        res=max(dfs(i,j),res)
        return res
        
