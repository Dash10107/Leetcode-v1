class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            n = len(s)
            temp = ''
            for i in range(n-1):
                t = (int(s[i])+int(s[i+1]))%10
                temp+= str(t)
            s = temp
        return s[0]==s[1]