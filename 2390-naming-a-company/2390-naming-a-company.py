class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic  = defaultdict(set)
        ans = 0
        for idea in ideas:
            dic[idea[0]].add(idea[1:])
        d = sorted(dic.items())
        for i1,d1 in d:
            for i2,d2 in d:
                if i2>=i1:break
                c = len(d1&d2)
                ans+= ((len(d1)-c)*(len(d2)-c))
        return ans*2