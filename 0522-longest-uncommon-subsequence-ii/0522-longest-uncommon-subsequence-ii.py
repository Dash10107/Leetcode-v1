class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(s,t):
            i=0
            for c in t:
                if i<len(s) and s[i]==c:
                    i+=1
            return i==len(s)
        strs.sort(key=len,reverse=True)
        for i,s in enumerate(strs):
            found = False
            for j,t in enumerate(strs):
                if i!=j and isSub(strs[i],strs[j]):
                    found = True
                    break
            if not found:
                return len(s)
        return -1