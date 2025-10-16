class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        freq = {}
        for s in s1:
            if s in freq.keys():
                freq[s]+=1
            else:
                freq[s]=1
        frame = len(s1)
        temp = {}
        for i in range(frame):
            if s2[i] in temp.keys():
                temp[s2[i]]+=1
            else:
                temp[s2[i]]=1
        if temp == freq:
            return True
        for i in range(frame,len(s2)):
            start = s2[i-frame]
            if temp[start]==1:
                del temp[start]
            else:
                temp[start]-=1
            end = s2[i]
            if end in temp.keys():
                temp[end]+=1
            else:
                temp[end]=1
            
            if temp == freq:
                return True
        return False

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        