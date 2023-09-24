# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=r51_ZifUdvU
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/is-subsequence/
    
#     I have added this question because there is another concept through which this can be solved as well (see approach-1 below). That concept may not be optimal
#     for this question but it helps to solve related questions optimally. Example : Leetcode-792 (Number of Matching Subsequences) asked by GOOGLE
#     My Code for Leetcode-792 using this approach - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Binary%20Search/Number%20of%20Matching%20Subsequences.cpp
# 

#***************************************************Python*************************************************/
# Follow Up Approach
# Approach-1 (Using Binary Search) -> This is an important concept for qns like Leetcode-792

#TODO






#***************************************************Python*************************************************/
#Approach-2 (Simplest O(n) approach)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)
        i,j = 0, 0
        while i<m and j<n:

            if s[i] == t[j]:
                i+=1
            
            j+=1
        
        return i == m
        

        