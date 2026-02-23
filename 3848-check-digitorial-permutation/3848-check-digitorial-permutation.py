class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        facts = [1]
        for i in range(1,10):
            facts.append(facts[-1]*i)
        ds = sum(facts[i] for i in map(int,str(n)))
        return Counter(str(n))==Counter(str(ds))