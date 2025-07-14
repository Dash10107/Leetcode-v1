class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        vis= [False]*n
        ans =0
        i = 0
        while 0<=i<n and not vis[i]:
            ins,val = instructions[i],values[i]
            vis[i]=True
            if ins=='add':
                ans+=val
                i+=1
            elif ins=='jump':
                i+=val
        return ans
            