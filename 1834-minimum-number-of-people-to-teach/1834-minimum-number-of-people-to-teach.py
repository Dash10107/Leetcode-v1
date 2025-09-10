class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        langs = [set(l) for l in languages]
        broken = set()
        for u,v in friendships:
            u-=1;v-=1
            if langs[u].isdisjoint(langs[v]):
                broken.add(u)
                broken.add(v)
        if not broken:return 0
        
        ans = float('inf')
        for i in range(1,n+1):
            teach = 0
            for u in broken:
                if not i  in langs[u]:
                    teach+=1
            ans = min(ans,teach)
        return ans