# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=SerANdwnELI
#     Company Tags                : Netflix, Google, Meta
#     Leetcode Link               : https://leetcode.com/problems/design-hashmap/
# 

# ************************************ Python ************************************

# Approach: Using chaining approach and using less space

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
    
    def _index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.table[idx]:
            self.table[idx] = ListNode(key,value)
            return
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                curr.next = ListNode(key,value)
            curr = curr.next

    def get(self, key: int) -> int:
        idx = self._index(key)
        curr = self.table[idx]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        curr = self.table[idx]
        if not curr:
            return 
        
        if curr.key == key:
            self.table[idx] = curr.next
            return 
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)