class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        sc = c.most_common()

        final=float('inf')
        for temp in c.values():
            ans = 0
            for i in range(len(sc)):
                if sc[i][1]<temp:
                    ans+= sc[i][1]
                elif sc[i][1]>temp+k:
                    ans+=  sc[i][1]-temp-k
            final = min(ans,final)
        return final