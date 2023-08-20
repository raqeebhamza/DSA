# Company Tags                : META, AMAZON
# Leetcode Link               : https://leetcode.com/problems/maximal-network-rank/


# ************************************************ python ********************************************************


# Algo:
# 1- Push real index with each element in edges list
# 2- Sort based on the weight of the edges
# 3- Find the MST Weight using -> kruskal algorithm
# 4- Check each edge and find weight using kruskal algorithm and find newWeight
        # -> skip  if newWeight > MSTweight: (critical edge)
        # -> add   if newWeight == MSTweight: (pseudo edge)

class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]
        self.count = n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def unionSet(self,x,y):
        xset, yset = self.find(x),self.find(y)
        if xset == yset:
            return 0
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            self.rank[xset] += self.rank[yset]
        else:
            self.parent[xset]=yset
            self.rank[yset]+=self.rank[xset]
        self.count-=1
        return 1
    def isConnected(self,x,y):
        return self.find(x)==self.find(y)
    def connectComp(self):
        return self.count
      
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def kruskal(edges, skipEdge,addEdge):
            currSum = 0
            uf = UnionFind(n)
            if addEdge !=-1:
                u,v,w,j = edges[addEdge]
                uf.unionSet(u,v)
                currSum += w
            for i in range(len(edges)):
                if i == skipEdge:
                    continue
                u,v,w,j = edges[i]
                parentU = uf.find(u)
                parentV = uf.find(v)
                if parentU!=parentV:
                    uf.unionSet(u,v)
                    currSum+=w
            if uf.connectComp()>1:
                return float('inf')
            return currSum
        for i in range(len(edges)):
            edges[i].append(i)
        
        edges.sort(key=lambda x: x[2])

        mstWeight = kruskal(edges,-1,-1)
        critical = []
        pseudoCritical = []
        for i in range(len(edges)):
            if kruskal(edges,i,-1)> mstWeight: # skipping ith edge
                critical.append(edges[i][3])
            elif kruskal(edges,-1,i) == mstWeight: # adding ith edge
                pseudoCritical.append(edges[i][3])
        
        return [critical,pseudoCritical]


        