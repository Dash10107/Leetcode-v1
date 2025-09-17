class Solution:
    def partitionString(self, s: str) -> int:
        flag=0;ans=1
        for ch in s: 
            val = ord(ch)
            if flag&(1<<val):
                ans+=1
                flag = 0
            flag |= 1<<val
        return ans 