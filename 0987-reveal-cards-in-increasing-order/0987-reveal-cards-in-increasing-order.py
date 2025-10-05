class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n =len(deck)
        res = [0]*n
        i,ind,skip=0,0,False
        while i<n:
            if res[ind]==0:
                if not skip:
                    res[ind]=deck[i]
                    i+=1
                skip = not skip
            ind=(ind+1)%n
        return res