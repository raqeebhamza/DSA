
# Leetcode Link   : https://leetcode.com/problems/sort-colors/
# Asked by        : Careem
#----------------------------------------------------------------------------------------------
# Time : O(n)

def sortColor(nums, pattern):
    hm = {}
    for n in nums:
        if n in hm:
            hm[n]+=1
        else:
            hm[n]=1 
    res = []
    for i in range(len(hm)):
        res += [i]*hm[i]
    res1 = []
    for i in pattern:
        res1 += [i]*hm[i]
    return [res,res1]

print(sortColor([0,2,2,0,4,0,1,2,3,3],[4,0,2,3,1]))

 