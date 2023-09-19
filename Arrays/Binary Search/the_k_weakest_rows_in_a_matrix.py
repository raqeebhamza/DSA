# 
#     YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=X1ZG-CXkmEM
#     Company Tags                : Amazon (Same variation : They just want to chec if you go for Binary Search as an improvement)
#     Leetcode Link               : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# 

# /***************************************** Python *****************************************/
# Approach-1 (Using Sorting + Binary Search)
# T.C : O(m*log(n)) + O(m*log(m))
# S.C : O(m) to store count of ones and corresponding row in the vector

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarySearch(arr,l,r):
            res = -1
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid] == 1:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res+1
        m = len(mat)
        n = len(mat[0])

        countOnes = []

        for row in range(m):
            numOfOnes = binarySearch(mat[row],0,n-1)
            countOnes.append((numOfOnes,row))
        
        countOnes.sort()
        res = []
        for i in range(k):
            res.append(countOnes[i][1])
        return res
