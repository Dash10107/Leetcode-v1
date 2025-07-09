class Solution:
    def characterReplacement(self, answer: str, k: int) -> int:
        n = len(answer)
        st = set(answer)
        res = 0
        for ch in st:
            l=0;ans=0;cnt=0
            for i in range(n):
                if answer[i]==ch:
                    cnt+=1
                while (i - l + 1) - cnt>k:
                    if answer[l]==ch:cnt-=1
                    l+=1
                ans = max(i-l+1,ans)
            res = max(ans,res)
        return res