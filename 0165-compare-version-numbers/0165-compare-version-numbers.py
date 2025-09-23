class Solution:
    def compareVersion(self, ver1: str, ver2: str) -> int:
        v11 = ver1.split('.')
        v22 = ver2.split('.')
        n = max(len(v11),len(v22))
        for i in range(n):
            s1 = int(v11[i]) if i<len(v11) else 0
            s2 = int(v22[i]) if i<len(v22) else 0
            # print(s1,s2)
            if s1>s2:return 1
            elif s2>s1:return -1
        return 0