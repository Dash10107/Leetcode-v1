class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n  = len(clips);ans=0
        i=0;curr=0;net=0
        while curr<time:
            while i<n and clips[i][0]<=curr:
                net = max(net,clips[i][1])
                i+=1
            if net==curr:
                return -1
            ans+=1
            curr=net
        return ans