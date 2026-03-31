class Solution:
    def generateString(self, S: str, T: str) -> str:
        n,m = len(S),len(T)
        ans = ['a'] * (n+m-1)
        fixed = [0]*(n+m-1)
        for i,c in enumerate(S):
            if c =='T':
                ans[i:i+m]=T
                fixed[i:i+m]= [1]*m
        for i,c in enumerate(S):
            window = ''.join(ans[i:i+m])
            if c =='T':
                if window!=T:
                    return ''
            elif window==T:
                for j in reversed(range(i,i+m)):
                    if not fixed[j]:
                        ans[j]='b'
                        break
                else:
                    return ''
                
        return ''.join(ans)    