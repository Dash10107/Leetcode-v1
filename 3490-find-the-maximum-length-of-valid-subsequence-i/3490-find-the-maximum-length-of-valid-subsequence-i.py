class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        odd = sum(1 for x in nums if x%2)
        even = n-odd
        altodd = True;c1 = 0
        for x in nums:
            if altodd and x%2:
                altodd = not altodd
                c1+=1
            elif not altodd and x%2==0:
                c1+=1
                altodd = not altodd
        alteven=True;c2 = 0
        for x in nums:
            if alteven and x%2==0:
                c2+=1
                alteven = not alteven
            elif not alteven and x%2:
                c2+=1
                alteven = not alteven
        return max(odd,even,c1,c2)