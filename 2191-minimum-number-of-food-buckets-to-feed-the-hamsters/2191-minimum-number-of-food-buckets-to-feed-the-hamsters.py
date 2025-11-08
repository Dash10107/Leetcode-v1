class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        ans = 0;n=len(hamsters)
        hamsters = list(hamsters)
        for i in range(len(hamsters)):
            if hamsters[i]=='H':
                left =hamsters[i-1] if i-1>=0 else ''
                right = hamsters[i+1] if i+1<n else ''
                if left=='D' or right=='D':
                    continue
                elif right=='.':
                    hamsters[i+1]='D'
                    ans+=1
                elif left=='.':
                    hamsters[i-1]='D'
                    ans+=1
                else:
                    return -1
        return ans