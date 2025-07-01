class Solution:
    def possibleStringCount(self, word: str) -> int:    
        tc = 1
        i = 0
        while i < len(word) :
            j = i
            while j <len(word) and word[j]==word[i]:
                j+=1
            l = j-i
            if l > 1:
                tc+=l-1
            i =j
        return tc
            