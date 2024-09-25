
# 
#     Youtube video : https://www.youtube.com/watch?v=PRHedN3h2Gc
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/sum-of-prefix-scores-of-strings
# 
# *********************************************************** Python ************************************************

# Approach  Using TRIE 
# T.C : O(n*l), n = number of words, l = average length of each word
# S.C : O(n*l), need to store all characters of words
class TrieNode:
    def __init__(self):
        self.next = [None]*26
        self.cnt = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = TrieNode()
            node.next[ord(c) - ord("a")].cnt +=1
            node = node.next[ord(c) - ord("a")]
    def count(self, s):
        node = self.root
        res = 0
        for c in s:
            res += node.next[ord(c)-ord("a")].cnt
            node = node.next[ord(c)-ord("a")]
        return res

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            scores[i] = self.count(words[i])
        return scores
    


        