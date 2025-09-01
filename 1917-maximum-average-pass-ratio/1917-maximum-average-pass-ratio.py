class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def pass_gain(p1,total):
            return (p1+1)/(total+1) - p1/total
        heap = []
        for pi,ti in classes:
            gain = pass_gain(pi,ti)
            heappush(heap,(-gain,pi,ti))
        for _ in range(extraStudents):
            gain,pi,ti = heappop(heap)
            pi+=1
            ti+=1
            new = pass_gain(pi,ti)
            heappush(heap,(-new,pi,ti))
        total_ratio = 0
        for _,pi,ti in heap:
            total_ratio += pi/ti
        return total_ratio/len(classes)
        