class Solution:
    def minMaxDifference(self, num: int) -> int:
        ans = 0
        man,mix = '',''
        found = 0
        for i in str(num):
            if i!='9':
                found = i
                break
        fo2 = 0
        for i in str(num):
            if i!=0:
                fo2 = i
                break
        for i in str(num):
            if i==found and i==fo2:
                man+='9'
                mix+='0'
            elif i == found:
                man += '9'
                mix += i
            elif fo2==i:
                mix+= '0'
                man += i
            else:
                man += i
                mix += i
        print(man,mix)
        return int(man)-int(mix)