class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:

        hmap=defaultdict(list)
        hmap[0].append(-1)
        total=0
        count=0

        for num in nums:
            total=(total+num)%k
            if total in hmap:
                lst=hmap[total]
                idx=bisect_left(lst,num)
                count+=idx
        
            hmap[total].append(num)

        return count