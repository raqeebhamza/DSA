# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=JlQEoNs263o
#     Company Tags                : META
#     Leetcode Link               : https://leetcode.com/problems/validate-binary-tree-nodes/
# 

# 
#   Find the DSU solution here - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Disjoint%20Set/Validate%20Binary%20Tree%20Nodes.cpp
# 

# ******************************************************** C++ ********************************************************/
# Approach-1 (Using simple BFS or DFS and Binary Tree Property)
# Find it in my "Binary Tree" repo
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        childToParentMap = defaultdict()
        adj = defaultdict(list)
        for i in range(n):
            node = i 
            leftC = leftChild[i]
            rightC = rightChild[i]

            if leftC != -1:
                if leftC in childToParentMap:
                    return False
                adj[i].append(leftC)
                childToParentMap[leftC] = i

            if rightC != -1:
                if rightC in childToParentMap:
                    return False
                adj[i].append(rightC)
                childToParentMap[rightC] = i
        
        root = -1

        for i in range(n):
            if i not in childToParentMap:
                if root != -1:
                    return False
                root = i
        
        if root == -1:
            return False
        
        count = 1
        que = deque()
        visited = set()
        que.append(root)
        visited.add(root)
        while que:
            node = que.pop()
            for v in adj[node]:
                if v not in visited:
                    visited.add(v)
                    count+=1
                    que.append(v)
        return count == n