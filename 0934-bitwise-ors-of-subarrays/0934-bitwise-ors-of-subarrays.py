class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        curr = set()
        ans = set()
        for n in arr:
            curr = {c|n for c in curr}
            curr.add(n)
            ans |= curr
        return len(ans)