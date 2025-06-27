class Solution:
    def checkRecord(self, s: str) -> bool:
        ab = 0
        la = 0
        for  i in range(len(s)):
            if s[i]=='A':
                la = 0
                if ab<1:ab+=1
                else:return False
            elif s[i]=='L':
                if la<2:la+=1
                else:return False
            else:
                la=0
        return True