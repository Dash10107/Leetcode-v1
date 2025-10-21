class Solution:
    def characterReplacement(self, answer: str, k: int) -> int:
        l,r,ans,mmf=0,0,0,0
        dic=defaultdict(int)
        while r<len(answer):
            dic[answer[r]]+=1
            mmf = max(mmf,dic[answer[r]])
            if (r-l+1)-mmf>k:
                dic[answer[l]]-=1
                l+=1
            if (r-l+1)-mmf<=k:ans=max(ans,(r-l+1))
            r+=1
        return ans