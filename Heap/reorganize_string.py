# Leetcode Link   : https://leetcode.com/problems/sliding-window-maximum/
# Asked by        : Microsoft, Amazon, Google, Meta

#********************************************** python *******************************************

# Approach - 1 Using Heap
# Algo:
# step-1 count frequencies
# step-2 add the heap
# step-3 while (pq): 
        # -> pop first 
        # if first != res[last]:
            # -> append to result and update heap frequency
        # else:
            # -> if pq is empty: return ""
            # -> pop second
            # -> append into result 
            # -> append the first one
# return result
# Time : O(nlogk)
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        pq = [(-count,char) for char, count in Counter(s).items()]
        heapify(pq)
        while pq:
            count1, char1 = heappop(pq)
            if not res or res[-1] != char1:
                res.append(char1)
                if count1+1!=0:
                    heappush(pq,(count1+1,char1))
            else:
                if not pq: return ''
                count2, char2 = heappop(pq)
                res.append(char2)
                if count2+1 != 0:
                    heappush(pq,(count2+1,char2))
                heappush(pq,(count1,char1))
        return "".join(res)

#************************************************* Python ****************************************
# Approach - 2  (Using odd/even placement)
# Algo:
# alternative approach using even/odds placing of the element 
# first time place the max frequent character with 1 over step(leaving 1 empty place)
# nextime start from index 1

#Time: O(N)
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        charCounts = Counter(s)
        maxCount,let = 0,''
        for char, count in charCounts.items():
            if count > maxCount:
                maxCount = count
                let = char
        
        if maxCount > (len(s)+1)//2:
            return ""
        res = ['']*len(s)
        idx = 0

        while charCounts[let] != 0:
            res[idx] = let
            idx+=2
            charCounts[let]-=1
        
        for char,count in charCounts.items():
            while count >0:
                if idx >= len(s):
                    idx = 1
                res[idx] = char
                idx += 2
                count -= 1

        return "".join(res)

