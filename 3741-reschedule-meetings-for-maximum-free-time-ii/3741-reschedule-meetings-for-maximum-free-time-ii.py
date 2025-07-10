class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0]*(n+1)
        gaps[0] = startTime[0]
        for i in range(1,n):
            gaps[i]= startTime[i]-endTime[i-1]
        gaps[-1]= eventTime-endTime[-1]
        pref,suff = [gaps[0]],[gaps[-1]]
        for i in range(1,len(gaps)-1):
            pref.append(max(gaps[i],pref[-1]))
        for i in range(len(gaps)-2,0,-1):
            suff.append(max(gaps[i],suff[-1]))
        suff.reverse()
        ans = 0
        for i,[s,e] in enumerate(zip(startTime,endTime)):
            dur = e-s
            l,r = gaps[i],gaps[i+1]
            bl = -1 if i==0 else pref[i-1]
            br = -1 if i==n-1 else suff[i+1]
            time = l+r
            if bl>=dur or br>=dur:
                time+=dur
            ans = max(ans,time)
        return ans