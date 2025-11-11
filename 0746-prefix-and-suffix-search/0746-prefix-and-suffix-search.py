class WordFilter:

    def __init__(self, words: List[str]):
        n = len(words)
        seen = set()
        self.pref=defaultdict(set)
        self.suff=defaultdict(set)
        for i in range(n-1,-1,-1):
            if words[i] in seen:continue
            seen.add(words[i])
            for j in range(1,len(words[i])+1):
                self.pref[words[i][:j]].add(i)
                self.suff[words[i][-j:]].add(i)

    def f(self, p: str, s: str) -> int:
        inter=self.pref[p]&self.suff[s]
        if not inter:return -1
        return max(inter)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)