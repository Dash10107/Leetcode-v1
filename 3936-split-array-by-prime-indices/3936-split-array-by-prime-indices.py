class Solution:
    def splitArray(self, nums: List[int]) -> int:           
        p = 2;num = len(nums)
        primes = set(range(2,num+1))
        while (p * p <= num):
            if (p in primes):
                for i in range(p * p, num+1, p):
                    if i in primes:primes.remove(i)
            p += 1
        s1=0;s2=0
        for i,n in enumerate(nums):
            if i in primes:
                s1+=n
            else:
                s2+=n
        return abs(s1-s2)