
# 
#     Company Tags                : Amazon, Apple
#     Leetcode Link               : https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# 

#********************************************* Python ************************************************

# Time: O(N)
# Space: O(N)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = defaultdict(list)
        res = []
        for i, e in enumerate(groupSizes):
            hm[e].append(i)
            if len(hm[e]) == e:
                res.append(hm[e])
                hm[e] = []
        return res