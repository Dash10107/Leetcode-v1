class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        pref = 0
        n1,n2,n3=len(s1),len(s2),len(s3)
        for i in range(min(n1,n2,n3)):
            if s1[i]==s2[i] and s2[i]==s3[i]:
                pref+=1
            else:break
        ans= (n1-pref)+(n2-pref)+(n3-pref)
        return ans if pref else -1