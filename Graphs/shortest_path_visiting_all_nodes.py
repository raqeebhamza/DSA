# 
#       YOUTUBE VIDEO ON THIS Qn    : https://www.youtube.com/watch?v=m73DRkEo8Ko
#       Company Tags                : GOOGLE
#       Leetcode Link               : https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# 

#************************************* Python ****************************************************

#T.C: O((2^n)*n)
#S.C: O((2^n)*n)
class Solution: # using bitmask to store the state of the node in queue
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n =  len(graph)
        if n == 1 or n == 0:
            return 0
        que = deque() # (node, mast)
        visited = set() # (node, pathmask)
        for i in range(n):
            maskVal  = (1 << i)
            que.append((i,maskVal))
            visited.add((i,maskVal))
        allVisitedState = (1 << n)-1  # 11111 => 2^(n-1) => (1 << n)-1 => pow(2,n-1)-1
        print(allVisitedState)
        path = 0
        while que: #BFS starts here
            queSize = len(que)
            path+=1
            print(que)
            while queSize:
                queSize-=1
                curr = que.pop()
                currNode = curr[0]
                currMask = curr[1]
                for neigh in graph[currNode]:
                    nextNode = neigh
                    nextMask = currMask | (1 << nextNode)
                    if nextMask == allVisitedState: # nextMask == 11111
                        return path
                    if (nextNode, nextMask) not in visited:
                        visited.add((nextNode,nextMask))
                        que.append((nextNode,nextMask))
        return -1

                    

