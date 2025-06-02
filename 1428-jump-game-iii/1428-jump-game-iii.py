class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        vis = [False]*len(arr)
        vis[start]=True
        ans = False
        while q:
            ind = q.popleft()
            vis[ind]=True
            if arr[ind]==0:
                return True
            if ind-arr[ind]>=0 and not vis[ind-arr[ind]]:
                q.append(ind-arr[ind])
            if ind+arr[ind]<len(arr) and not vis[ind+arr[ind]]:
                q.append(ind+arr[ind])
        return False
                