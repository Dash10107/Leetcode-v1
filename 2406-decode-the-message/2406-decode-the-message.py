class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = 'abcdefghijklmnopqrstuvwxyz'
        dic = {' ':' '};i=0
        for ch in key:
            if ch not in dic:
                if i<len(s):
                    dic[ch]=s[i]
                    i+=1
        ans = ''
        for m in message:
            ans+= dic[m]
        return ans
