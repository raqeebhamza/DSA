
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=M0lhTkhUlp4
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# 

# ******************************************************** Python ***************************************************/
# Approach-1 (Simply simulate whatever the problem asks for)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prevSize = len(students)
        currCount = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                prevSize = len(students)
                currCount = 0
            else:
                ele = students.pop(0)
                students.append(ele)
                currCount += 1
            if currCount == prevSize:
                return currCount
        return 0

# ******************************************************** Python ***************************************************
# Aproach-2 (Using counter only)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        student0 = 0
        student1 = 0
        for s in students:
            student0 += s==0
            student1 += s==1
        
        for s in sandwiches:
            if s == 0 and student0 > 0:
                student0 -= 1
            elif s==1 and student1>0:
                student1 -= 1
            else:
                break
        return student0+student1
                