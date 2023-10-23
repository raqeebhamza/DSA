# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=0PFE_7S3X-U
#     Company Tags                : Google, Twitter, Facebook, Netflix
#     Leetcode Link               : https://leetcode.com/problems/flatten-nested-list-iterator/
# 

# ************************************************* C++ *************************************************/

# Approach-1 (Using stack of NestedInteger objects)
#
#     Always remember, if there is a nested structure and you need to flatten it, 
#     stack can help most of the times. For example : flatten linkedlist, doubly linkedlist etc.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stack = []
#         for i in range(len(nestedList)-1,-1,-1):
#             self.stack.append(nestedList[i])
    
#     def next(self) -> int:
#         num = self.stack.pop().getInteger()
#         return num
    
#     def hasNext(self) -> bool:
#         if not self.stack:
#             return False
        
#         while self.stack:
#             if self.stack[-1].isInteger():
#                 return True
#             curr = self.stack.pop()
#             innerList = curr.getList()
#             for i in range(len(innerList)-1,-1,-1):
#                 self.stack.append(innerList[i])
        
#         return False
    
class NestedIterator:
    def flatten(self,nestedList):
        for i in range(len(nestedList)):
            if nestedList[i].isInteger():
                self.que.append(nestedList[i].getInteger())
            else:
                self.flatten(nestedList[i].getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.que = []
        self.flatten(nestedList)
    def next(self) -> int:
        num = self.que.pop(0)
        return num
    
    def hasNext(self) -> bool:
        return True if len(self.que) else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())