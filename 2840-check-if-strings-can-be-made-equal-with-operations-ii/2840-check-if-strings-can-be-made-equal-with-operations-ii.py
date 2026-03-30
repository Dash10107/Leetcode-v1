class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even,odd = '',''
        targe,targo = '',''
        n = len(s1)
        for i in range(n):
            if i&1:
                odd+=s1[i]
                targo+=s2[i]
            else:
                even+=s1[i]
                targe+=s2[i]
        return (sorted(even)==sorted(targe)) and (sorted(odd)==sorted(targo))