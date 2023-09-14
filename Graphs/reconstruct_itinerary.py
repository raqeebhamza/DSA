
# 
#       Company Tags                : GOOGLE
#       Leetcode Link               : https://leetcode.com/problems/reconstruct-itinerary/
# 

#******************************************************** Python ********************************************************/
# Approach-1 (Using adj of string to vector and sorting it)
# T.C : O(V^2)
#Algo:
#Create adj list
#Sort neighbour lists of each node
#Traverse DFS on it and implement backtracking in it
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)

        numTickets = len(tickets)

        for fr,to in tickets:
            adj[fr].append(to)
        
        for key,v in adj.items(): # sorting for lexical order
            adj[key].sort()
        
        def dfs(fromAirport,path,res):
            path.append(fromAirport)
            print (path, numTickets)
            if len(path) == (numTickets+1):
                res.extend( path[:])
                return True
            
            neighbours = adj[fromAirport]

            for i in range(len(neighbours)):
                toAirport = neighbours[i]
                # remove it from list to save from cycle.
                del neighbours[i]
                if dfs(toAirport,path,res):
                    return True
                # add the removed element
                neighbours.insert(i,toAirport)
            path.pop()
            return False
        res = []
        dfs("JFK",[],res)
        return res








        