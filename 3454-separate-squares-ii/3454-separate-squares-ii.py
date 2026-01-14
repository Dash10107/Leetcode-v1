class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events =  []
        for x,y,l in squares:
            events.append((y,1,x,x+l))
            events.append((y+l,-1,x,x+l))
        events.sort()
        xs = [];areas = []
        prevy = events[0][0]
        ans = 0
        def func(intervals):
            intervals.sort()
            res=curr=0
            end = float('-inf')
            for a,b in intervals:
                if a>end:
                    res+= b-a
                    end = b
                elif b>end:
                    res+= b-end
                    end =b
            return res
        for y,typ,x1,x2 in events:
            if y>prevy and xs:
                h = y-prevy
                w = func(xs)
                areas.append((prevy,h,w))
                ans+= h*w
            if typ==1:
                xs.append((x1,x2))
            else:
                xs.remove((x1,x2))
            prevy= y
        half = ans/2
        acc = 0
        for y,h,w in areas:
            if acc + h*w >=half:
                return y+ (half-acc)/w
            acc+= h*w
        return 0.0
