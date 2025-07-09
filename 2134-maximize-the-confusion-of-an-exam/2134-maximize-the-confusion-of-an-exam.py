class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        n = len(answer)
        l=0;ans=0;cnt=0
        for i in range(n):
            if answer[i]=='F':
                cnt+=1
            while cnt>k:
                if answer[l]=='F':cnt-=1
                l+=1
            ans = max(i-l+1,ans)
        l = 0;cnt=0
        for i in range(n):
            if answer[i]=='T':
                cnt+=1
            while cnt>k:
                if answer[l]=='T':cnt-=1
                l+=1
            ans = max(i-l+1,ans)
        return ans