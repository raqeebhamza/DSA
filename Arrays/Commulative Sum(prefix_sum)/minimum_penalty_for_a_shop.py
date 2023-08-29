# 
#     Company Tags                : STRIPE, GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/minimum-penalty-for-a-shop/
# 

#********************************************* Python ************************************************

# Time: O(N)
# Space: O(N)
class Solution:
    def bestClosingTime(self, customers: str) -> int:

        prefixN = [0] * (len(customers)+1)
        suffixY = [0] * (len(customers)+1)

        for i in range(len(customers)):
            prefixN[i+1] = prefixN[i]
            if customers[i] == 'N':
                prefixN[i+1] += 1
        
        for i in range(len(customers)-1,-1,-1):
            suffixY[i] = suffixY[i+1]
            if customers[i] == 'Y':
                suffixY[i] += 1
            
        minPenalty = float('inf')
        minHour = float('inf')
        for i in range(len(customers)+1):
            currP = suffixY[i]+prefixN[i]
            if minPenalty>currP:
                minPenalty = currP
                minHour = i
        
        return minHour

# Time: O(N)
# Space: O(1)
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minPenalty = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                minPenalty += 1
        penalty = minPenalty
        minHour = 0
        for i in range(1, len(customers)):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < minPenalty :
                minPenalty = penalty
                minHour = i+1
        return minHour
        



            



        
        

        


