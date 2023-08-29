
# 
#     Company Tags                : AMAZON, GOOGLE, BLOOMBERG, PAYPAL
#     Leetcode Link               : https://leetcode.com/problems/implement-stack-using-queues/
# 

#********************************************* Python ************************************************

# Time: O(n) 
# Approach-1 -> using 2 queues 
class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.popleft())
        
        self.que1 = deque(self.que2.copy())
        self.que2 = []

    def pop(self) -> int:
        return self.que1.popleft()

    def top(self) -> int:
        return self.que1[0]

    def empty(self) -> bool:
        return len(self.que1)==0

# Approach-2  -> using 1 queue
class MyStack: 

    def __init__(self):
        self.que1 = deque([])

    def push(self, x: int) -> None:
        self.que1.append(x)
        i = 0
        while i<len(self.que1)-1:
            self.que1.append(self.que1.popleft())
            i+=1

    def pop(self) -> int:
        return self.que1.popleft()

    def top(self) -> int:
        return self.que1[0]

    def empty(self) -> bool:
        return len(self.que1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()