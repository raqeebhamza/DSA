
#     	Leetcode Link 		    : https://leetcode.com/problems/01-matrix/
#     	Company Tags  		    : Google
# 


# Why BFS ?
# Always remember whenever you have to find shortest path in graph, 2-d matrix , BFS
# must come to your mind first.

# Kind of similar qn : "Walls And Gates" https://leetcode.com/problems/walls-and-gates/
# */

# ************************************************************ Python  ************************************************************
# Approach (Using BFS) Time : O(m*n)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        dir = ((1,0),(0,1),(-1,0),(0,-1))
        m,n = len(mat),len(mat[0])
        
        res = [[-1]*n for _ in range(m)]
        que = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    que.append((i,j))
        
        #BFS start here
        while que:
            idx = que.popleft()
            for i,j in dir:
                newi = idx[0]+i
                newj = idx[1]+j
                if newi < m and newi >= 0 and newj < n and newj >= 0 and res[newi][newj] == -1:
                    res[newi][newj] = res[idx[0]][idx[1]] + 1
                    que.append((newi,newj))
                
        return res