# Company Tags                : MICROSOFT, TESLA
# Leetcode Link               : https://leetcode.com/problems/maximal-network-rank/


# ************************************************ python ********************************************************
#Time: O(E+v^2)

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(set)

        for src,dst in roads:
            adj[src].add(dst)
            adj[dst].add(src)

        res = 0
        for i in range(n):
            for j in range(i+1,n):
                currRank = len(adj[i])+len(adj[j])
                if j in adj[i]: # same edge must count one time for both cities.
                    currRank -= 1
                res = max(res,currRank)
        
        return res
