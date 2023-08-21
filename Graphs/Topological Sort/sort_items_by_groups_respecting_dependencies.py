# /*
#       Company Tags                : AMAZON SDE 2
#       Leetcode Link               : https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# */


# Algo: 
# ----- create items graph, create Item In degree
# ----- create group graph, create group In degree
# ----- call topological sort on both 
#                      -> will get items order
#                      -> will get group order
# ----- iterate over items order and append that item in specific order.
# ----- returnt that new item list

# ************************************************************** python *************************************************************

# Time Complexity - 
# We fill the itemGraph and groupGraphs by traversing on each item and beforeItems causing O(n^2) in worst case. 
# After that, Since we call Topological Sort for : 
# 1) itemGraph - O(n + edges) 
# 2) Group Graph - O(m + edges) 

# Then, we run for loop ok itemOrder - O(n) 
# Then we run for loop on groupOrder - O(m) 
# Then at the end we make result - O(n)
# After summing up all, the biggest term is O(n^2) 
# Hence worst case TC = O(n^2) Hope this helps. 

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(adj, indegree): # using kahn's algorithm
            que = deque([])

            for i in range(len(adj)):
                if indegree[i]==0:
                    que.append(i)
            
            sortedRes = []
            while que:
                node = que.pop()
                sortedRes.append(node)
                for i in adj[node]:
                    indegree[i] -= 1
                    if indegree[i]==0:
                        que.append(i)
            return sortedRes if len(sortedRes) == len(adj) else []

        # assigning groups to -1 items
        for i in range(n):
            if group[i] == -1:
                group[i] = m 
                m += 1
        
        # step-1 Make Items graph and itemIndegree
        itemGraph = [[] for _ in range(n)]
        itemIndegree = [0]*n
        # step-2 Make group graph and group Indegree
        groupGraph =  [[] for _ in range(m)]
        groupIndegree = [0]*m
        
        # Fill those graphs and indegrees
        for i in range(n):
            for prev in beforeItems[i]:
                itemGraph[prev].append(i)
                itemIndegree[i] += 1

                if group[i] != group[prev]:
                    prevItemGroup = group[prev]
                    currItemGroup = group[i]
                    groupGraph[prevItemGroup].append(currItemGroup)
                    groupIndegree[currItemGroup] += 1
        
        # step - Topological sorting
        itemOrder = topologicalSort(itemGraph, itemIndegree)
        groupOrder = topologicalSort(groupGraph,groupIndegree)
        # iterate over the items order and place in seperate groups in sorted order

        groupToItemInOrder = defaultdict(list)
        for item in itemOrder:
            itemGroup = group[item]
            groupToItemInOrder[itemGroup].append(item)

        res = []
        for grp in groupOrder:
            res += groupToItemInOrder[grp]
        
        return res
                







