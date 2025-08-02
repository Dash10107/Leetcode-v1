class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        odds,evens = [],[]
        targo,targe = [],[]
        nums.sort();target.sort()
        for a,b in zip(nums,target):
            if a&1:odds.append(a)
            else:evens.append(a)
            if b&1:targo.append(b)
            else:targe.append(b)
        ops = 0
        for a,b in zip(odds,targo):
            diff = abs(a-b)
            ops+= (diff//2)
        for a,b in zip(evens,targe):
            diff = abs(a-b)
            ops+= (diff//2)
        return ops//2