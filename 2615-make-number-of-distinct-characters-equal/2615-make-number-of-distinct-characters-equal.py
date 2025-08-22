class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for ch in c1:
            for ch2 in c2:
                nc1,nc2 = c1.copy(),c2.copy()
                nc1[ch]-=1
                if nc1[ch]==0:
                    del nc1[ch]
                nc2[ch2]-=1
                if nc2[ch2]==0:
                    del nc2[ch2]
                nc1[ch2]+=1
                nc2[ch]+=1
                if len(nc1)==len(nc2):
                    return True
        return False