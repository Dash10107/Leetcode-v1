class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = '';n=len(num)
        for i in range(len(num)):
            if i+2<n and num[i]==num[i+1] and num[i+1]==num[i+2]:
                s = max(s,num[i:i+3])
        return s