class Solution:
    def countComponents(self, nums, threshold):
        n = len(nums)
        dic = {};dic2=defaultdict(int)
        def find(x):
            if x not in dic:
                return x
            if x!=dic[x]:
                dic[x]=find(dic[x])
            return dic[x]
        def union(x,y):
            a,b=find(x),find(y)
            if a!=b:
                dic[b]=a
        def facs(x):
            ans=set();y=x
            while y<=threshold:
                ans.add(y)
                y+=x
            return ans
        
        for i in range(n):
            fact = facs(nums[i])
            for j in fact:
                union(j,nums[i])
        
        for i in nums:
            dic2[find(i)]+=1
        return len(dic2)
        

            