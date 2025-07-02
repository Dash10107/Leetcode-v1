class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = []
        ans = ['']*len(s)
        for i,ch in enumerate(s):
            if ch.isalpha():
                temp.append(ch)
            else:
                ans[i]=ch
        j = 0
        for ch in temp[::-1]:
            while ans[j]!='':
                j+=1
            ans[j]=ch
        return ''.join(ans)