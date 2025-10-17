class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans,inc=0,0
        for i in range(len(target)):
                if inc<target[i]:
                    ans+= target[i]-inc
                inc=target[i]
        return ans