class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def get_primes(x):
            d ={}
            i = 2
            while i*i <=x:
                if x%i==0:
                    d[i]=1
                    while x%i==0:
                        x//=i
                i+=1
            if x>1:
                d[x]=i
            return d.keys()
        n = len(nums)
        last = {}
        for i,x in enumerate(nums):
            for p in get_primes(x):
                last[p]=i
        ans = 0
        for i,x in enumerate(nums):
            for p in get_primes(x):
                ans = max(ans,last[p])
            if i==ans and i<n-1:
                return i
        return -1
            
