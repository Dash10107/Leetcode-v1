class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        mp = defaultdict(int)
        for s,e in intervals:
            mp[s]+=1
            mp[e]-=1
        mp[new[0]]+=1
        mp[new[1]]-=1
        c=0;ans=[]
        start=-1
        for x  in sorted(mp.keys()):
            if c==0:start=x
            c+=mp[x]
            if c==0:
                ans.append([start,x])
        return ans