class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9+7
        q = deque([0]*forget)
        q[-1]=1
        total=1;share=0
        for day in range(1,n):
            temp = q.popleft()
            total-=temp
            share-=temp
            count = q[-delay]
            share = (share+count)%mod
            q.append(share)
            total= (total+share)%mod
        return total%mod