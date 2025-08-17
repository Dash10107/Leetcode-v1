class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        si = {s:i for i,s in enumerate(req_skills)}
        cand = []
        for ss in people:
            val = 0
            for s in ss:
                val |= 1<< si[s]
            cand.append(val)
        @cache
        def func(i,mask):
            if mask==0:return []
            if i==len(people):return [0]*100
            if not (mask & cand[i]):return func(i+1,mask)
            return min(func(i+1,mask),[i]+ func(i+1,mask & ~cand[i]),key=len)
        return func(0,(1<<len(req_skills))-1)