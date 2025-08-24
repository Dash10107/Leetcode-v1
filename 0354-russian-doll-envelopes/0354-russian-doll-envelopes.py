class Solution:
    def maxEnvelopes(self, envs: List[List[int]]) -> int:
        envs.sort(key=lambda x:(x[0],-x[1]))
        n = len(envs)
        lis = []
        heights = [h for w, h in envs]
        for num in heights:
            pos = bisect.bisect_left(lis,num)
            if pos <len(lis):
                lis[pos]=num
            else:
                lis.append(num)
        return len(lis)