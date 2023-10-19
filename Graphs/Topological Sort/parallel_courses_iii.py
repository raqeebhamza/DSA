
# /*
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=743cYtf3DJI
#     Company Tags                : Uber
#     Leetcode Link               : https://leetcode.com/problems/parallel-courses-iii/
# */

# /****************************************************** Python ******************************************************/
# //Approach-1 (Using Simple Topological sorting)
# //T.C : O(V+E)



#Topological sort
#- find Indegree
#- put element in queue having indegree == 0
#- queue traversal
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        maxTime = [0]*n
        adj = defaultdict(list)
        indegree = [0]*n
        for i in range(len(relations)):
            u = relations[i][0] - 1
            v = relations[i][1] - 1
            adj[u].append(v)
            indegree[v] += 1
        
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i)
                maxTime[i] = time[i]
        
        while que:
            u = que.pop()
            for v in adj[u]:
                indegree[v] -= 1
                maxTime[v] = max(maxTime[v],maxTime[u]+time[v])
                if indegree[v] == 0:
                    que.append(v)
        
        return max(maxTime)
                

