class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        time=0;ans=0
        heap=[]
        for dur,last in courses:
            if time+dur<=last:
                time+=dur
                heappush(heap,-dur)
                ans+=1
            else:
                if heap and dur<(-heap[0]):
                    time+=heappop(heap)
                    time+=dur
                    heappush(heap,-dur)
        return ans