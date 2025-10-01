class Solution:
    def goodDaysToRobBank(self, sec: List[int], time: int) -> List[int]:
        n = len(sec)
        if time==0:return list(range(n))
        nonInc,nonDec = [0]*n,[0]*n
        for i in range(1,n):
            if sec[i]<=sec[i-1]:nonInc[i]=nonInc[i-1]+1
            
        for i in range(n-2,-1,-1):
            if sec[i]<=sec[i+1]:nonDec[i]=nonDec[i+1]+1
            
        ans = []
        for i in range(n):
            if nonInc[i]>=time and nonDec[i]>=time:ans.append(i)
        return ans