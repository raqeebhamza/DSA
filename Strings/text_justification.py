# 
#     Company Tags                : AMAZON, GOOGLE, Uber
#     Leetcode Link               : https://leetcode.com/problems/text-justification/
# 

#********************************************* Python ************************************************

#Algo:
# while (len(words)) # untill cover all the words
#   step1- create list of words that can fit in one line
#   step2- use those words and calculate extra spaces and add those spaces in between
# return the appended lines as result.

#  Time: O(n⋅k)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def getWords(i):
            currLineWords = []
            currLen = 0

            while i<len(words) and currLen+len(words[i])<=maxWidth:
                currLineWords.append(words[i])
                currLen += len(words[i])+1
                i+=1
            
            return currLineWords
        

        def createLine(line,i):
            baseLen = -1
            for word in line:
                baseLen += len(word)+1
            
            extraSpaces = maxWidth-baseLen

            if len(line) == 1 or i == len(words):
                return " ".join(line)+ " "*extraSpaces
            
            wordCount = len(line)-1
            spacePerWord = extraSpaces//wordCount
            needExtraSpace = extraSpaces % wordCount

            for j in range(needExtraSpace):
                line[j] += " "
            
            for j in range(wordCount):
                line[j] += " "*spacePerWord
            
            return " ".join(line)
        
        res = []

        i=0
        while i<len(words):
            currLineWords = getWords(i)
            print(currLineWords)
            i += len(currLineWords)
            res.append(createLine(currLineWords,i))
        
        return res