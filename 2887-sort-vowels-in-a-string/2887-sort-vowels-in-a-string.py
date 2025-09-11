class Solution:
    def sortVowels(self, s: str) -> str:
        st = {'a','e','i','o','u',"A",'E','I','O','U'}
        ans = []
        for ch in s:
            if ch in st:ans.append(ch)
        ans.sort()
        i = 0;n=len(s)
        t = ''
        for j in range(n):
            if s[j] in st:
                t+= ans[i]
                i+=1
            else:
                t+=s[j]
        return t