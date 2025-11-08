class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        line = defaultdict(int)
        for s,e in flowers:
            line[s]+=1
            line[e+1]-=1
        times = sorted(line.keys())
        people = [(t, i) for i, t in enumerate(people)]
        people.sort()
        ans = [0]*len(people);curr=0;i=0
        for t,idx in people:
            while i<len(times) and times[i]<=t:
                curr+=line[times[i]]
                i+=1
            ans[idx]=curr
        return ans