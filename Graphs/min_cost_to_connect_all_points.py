
# 
#     MY YOUTUBE VIDEO ON THIS Qn :      Using Prim's     - https://www.youtube.com/watch?v=hsr7KolYDH0
#     				                     Using Kruskal's  - https://www.youtube.com/watch?v=O6wQQtv71S0
#     Company Tags                : META
#     Leetcode Link               : https://leetcode.com/problems/min-cost-to-connect-all-points/
# 

# //Approach-1 (Using Priority_queue and Adjacency list representation of graph) - Prim's Algorithmclass Solution:
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
    def calculateDist(x1,x2,y1,y2): # manhattan distance
        a = abs(x1-x2)
        b = abs(y1-y2)
        return a+b
    
    def PrimsAlgo(adj, numberOfVertices):
        cost = 0
        minHeap = [(0,0)]
        inMST = [False]*numberOfVertices
        while minHeap: # E
            w, u = heappop(minHeap) #log(E)
            if not inMST[u]:
                inMST[u] = True
                cost += w 
                for neighbor in adj[u]:
                    neig = neighbor[0]
                    dist = neighbor[1]
                    heappush(minHeap, (dist,neig)) #log(E)
        return cost

    n = len(points)
    adj = defaultdict(list)
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            dist = calculateDist(points[i][0],points[j][0],points[i][1],points[j][1])
            adj[i].append((j,dist))
            adj[j].append((i,dist))

    return PrimsAlgo(adj,n)









        
