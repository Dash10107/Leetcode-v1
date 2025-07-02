class Solution:
    def calculateScore(self, s: str) -> int:
        stacks = [[] for _ in range(26)]
        ans = 0
        for i,ch in enumerate(s):
            v = ord(ch)-97
            if stacks[25-v]:ans+= i-stacks[25-v].pop()
            else:stacks[v].append(i)
        return ans