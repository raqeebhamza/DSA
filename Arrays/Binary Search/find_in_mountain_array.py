

# 
#     MY YOUTUBE VIDEO ON THIS QN : https://www.youtube.com/watch?v=wzHmgBIdQXA
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/find-in-mountain-array/
# 

# You can see my video on finding "Peak Index in a Mountain Array" - 
#     Code Link - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Binary%20Search/Peak%20Index%20in%20a%20Mountain%20Array.cpp
#     YouTube Video Link - https://www.youtube.com/watch?v=Op07kT-LoH8
# 

# ********************************************************* Python **************************************************************
# Approach - Solving using Binary Search
# T.C : log(n)
# S.C : O(1)

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeakIdx():
            l,r = 0,mountain_arr.length()-1
            while l<r:
                mid = l + ((r-l)//2)
                if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    l = mid+1
                else:
                    r = mid
            return l
        
        def binarySearch(mountainArr,l,r):
            while l<=r:
                mid = l+((r-l)//2)
                if mountainArr.get(mid) == target:
                    return mid
                elif mountainArr.get(mid) > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        def reverseBinarySearch(mountainArr,l,r):
            while l <= r:
                mid = l+((r-l)//2)
                if mountainArr.get(mid) == target:
                    return mid
                elif mountainArr.get(mid) > target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        peakIdx = findPeakIdx()
        idx = binarySearch(mountain_arr,0,peakIdx)
        if idx == -1:
            idx = reverseBinarySearch(mountain_arr,peakIdx,mountain_arr.length()-1)
        return idx





        