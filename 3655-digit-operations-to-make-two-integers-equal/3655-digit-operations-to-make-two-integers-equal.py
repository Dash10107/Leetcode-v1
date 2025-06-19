class Solution:
    def __init__(self):
        limit = 10000
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, limit + 1, i):
                    is_prime[j] = False
        self.primes = is_prime
    def minOperations(self, n: int, m: int) -> int:
        if self.primes[n] or self.primes[m]:
            return -1
        if m==n:
            return n
        dist = [float('inf')] * 10000
        dist[n]=n
        heap = [(n,n)]
        l = len(str(n))
        def neg(node, l):
            negs = []
            s = str(node)  # Ensure leading zeros if needed
            for i in range(len(s)):
                dig = int(s[i])
                for delta in [-1, 1]:
                    nd = dig + delta
                    if 0 <= nd <= 9:
                        sb = list(s)
                        sb[i] = str(nd)
                        new_val = int(''.join(sb))
                        if not self.primes[new_val]:
                            negs.append(new_val)
                        
            return negs
            negs = []
            s = str(node)
            for i in range(len(s)):
                dig = s[i]-'0'
                if dig<9:
                    sb = s
                    sb[i]=dig+1+'0'
                    if int(sb) not in self.primes:
                        negs.append(int(sb))
                if dig>0:
                    sb = s
                    sb[i]=dig-1+'0'
                    if int(sb) not in self.primes:
                        negs.append(int(sb))
            return negs
        while heap:
            cost,node = heapq.heappop(heap)
            if cost>dist[node]:
                continue
            if node==m:
                return cost
            for nx in neg(node,l):
                if nx+cost<dist[nx]:
                    dist[nx]=nx+cost
                    heapq.heappush(heap,(nx+cost,nx))
        return -1

