class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        n = len(nums)
        odd,even = [],[]
        for i in nums:
            if i&1:odd.append(i)
            else:even.append(i)
        if len(even)==n or len(even)==0:return True
        m = min(even);ok=True
        for o in odd:
            if o-m<1:
                ok=False
                break
        m = min(odd);ok=True
        for e in even:
            if e-m<1:
                ok=False;break
        return ok