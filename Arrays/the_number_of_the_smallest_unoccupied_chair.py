

# 
# 	MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=NePJRPCuOwg
#   Company Tags  		    : Uber, Facebook, Amazon, Yelp, Google, Snapchat, Amazon, Cisco - Qn had small Variations
#   Leetcode Link 		    : https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
# 


# *********************************************************************Python ************************************************************************/
# Approach-1 (Naive O(n^2) approach that comes to mind first)
# T.C : O(n^2)
# S.C : O(n)
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        chairs = [-1]*n
        targetFriendArrivalTime = times[targetFriend][0]
        times.sort()
        for a, d in times:
            for i in range(n):
                if chairs[i] <= a:
                    chairs[i] = d
                    if a == targetFriendArrivalTime:
                        return i
                    break
    

# Approach-2 (Using min-heaps)
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        occupied = [] # (departureTime, chair No)
        free = [] # (chair No)

        targetFriendArrivalTime = times[targetFriend][0]

        times.sort()
        chairNo = 0

        for a, d in times:

            while len(occupied) and occupied[0][0] <= a:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free, chair)

            if len(free):
                chair = heapq.heappop(free)
            else:
                chair = chairNo
                chairNo +=1
            if a==targetFriendArrivalTime:
                return chair
            
            heapq.heappush(occupied, (d, chair))
                
        return -