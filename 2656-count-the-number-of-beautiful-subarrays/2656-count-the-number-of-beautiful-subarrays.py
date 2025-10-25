class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n=len(nums);ans=0
        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]^nums[i]
        dic = defaultdict(int);dic[0]=1
        for i in range(1,n+1):
            if pref[i] in dic:
                ans+=dic[pref[i]]
            dic[pref[i]]+=1
        return ans