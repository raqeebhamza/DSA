
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=r2LPa779amQ
#     Company Tags                : 
#     Leetcode Link               : https://leetcode.com/problems/time-needed-to-buy-tickets/
# 

# ********************************************************** Python **************************************************/
# Approach-1 (Using Queue to simply simulate the operations)
# T.C : O(n*m) -> Loop runs intil queue is empty and in worst case all people have maximum m tickets 
# S.C : O(n)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        time = 0
        while queue:
            time += 1
            front = queue.popleft()
            tickets[front] -= 1
            if k == front and tickets[front] == 0:
                return time
            if tickets[front] != 0:
                queue.append(front)
        return time

# Approach-2 (Using simple observation)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[k], tickets[i])
            else:
                time += min(tickets[k] - 1, tickets[i])
        return time
    
    