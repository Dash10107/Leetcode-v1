class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        targ = set(target)
        curr = set()
        for i in range(1,n+1):
            if i in targ:
                ans.append("Push")
                curr.add(i)
            else:
                ans.append("Push")
                ans.append("Pop")
            if curr==targ:
                break
        return ans