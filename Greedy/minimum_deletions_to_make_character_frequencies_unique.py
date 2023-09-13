# 
#       Company Tags                : Atlassian, Adobe, Twitter
#       Leetcode Link               : https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


#************************************************python *****************************************

#Approach-1 (Using unordered set to keep track of frequencies)
#T.C : O(n) we don't visit any character more than once.
#S.C : O(n) - Set and note that freq is of size 26 which is of constant size
class Solution:
    def minDeletions(self, s: str) -> int:
        hashSet = set()
        counts = Counter(s)
        decrease = 0
        for k, v in counts.items():
            while v in hashSet and v > 0:
                v-=1
                decrease+=1
            hashSet.add(v)
        return decrease

#************************************************python *****************************************

#Approach-2 (Without using unordered_set)
# T.C : O(n) we don't visit any character more than once and sorting freq is O(26log26) = O(1)
# S.C : O(1) - Note that freq is of size 26 which is of constant size
class Solution:
    def minDeletions(self, s: str) -> int:

        freq = [0]*26

        for c in s:
            freq[ord(c)-ord('a')] += 1

        freq.sort()
        res = 0
        for i in range(len(freq)-2,-1,-1):
            if freq[i] >= freq[i+1]:
                prev = freq[i]
                freq[i] = max(0,freq[i+1]-1)
                res += prev-freq[i]
    
        return res
                