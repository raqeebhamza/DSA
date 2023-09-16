# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=QIu9HeyEjPc
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/path-with-minimum-effort/
# 

#Approach-1 : Using Dijkstra's Algo
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        isSafe = lambda x, y: 0 <= x < m and 0 <= y < n
        minHeap = []
        directions = ((-1,0),(0,-1),(1,0),(0,1))
        m = len(heights)
        n = len(heights[0])

        res = [[float('inf')]*n for _ in range(m)]

        res[0][0] = 0
        heappush(minHeap,(0,(0,0)))
        while minHeap:
            diff, coordinates = heappop(minHeap)
            i, j = coordinates

            for x,y in directions:
                newi = i+x
                newj = y+j

                if isSafe(newi,newj):
                    absDiff = abs(heights[newi][newj]-heights[i][j])
                    maxDiff = max(diff,absDiff)

                    if res[newi][newj] > maxDiff:
                        res[newi][newj] = maxDiff
                        heappush(minHeap,(maxDiff,(newi,newj)))
            
        return res[m-1][n-1]




            

