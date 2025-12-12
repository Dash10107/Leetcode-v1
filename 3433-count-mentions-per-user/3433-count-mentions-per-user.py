class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        ans = [0]*n
        status = [0]*n
        def users(ms,t):
            if ms=='ALL':
                return list(range(n))
            elif ms=='HERE':
                return [i for i,n in enumerate(status) if n<=t]
            else:
                ms =  ms.split(' ')
                return [int(i[2:]) for i in ms]
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        for m,t,ms in events :
            if m=='MESSAGE':
                ms = users(ms,int(t))
                for idd in ms:
                    ans[idd]+=1
            else:
                idd = int(ms)
                status[idd]= int(t)+60
        return ans