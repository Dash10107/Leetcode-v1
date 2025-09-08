class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isprime(n):
            if n <= 1:
                return False  # Numbers less than or equal to 1 are not prime
            if n <= 3:
                return True   # 2 and 3 are prime
            if n % 2 == 0 or n % 3 == 0:
                return False  # Exclude multiples of 2 and 3
            
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        i,j = len(nums),-1
        for k,n in enumerate(nums):
            if isprime(n):
                i = min(i,k);j=max(j,k)
        return j-i