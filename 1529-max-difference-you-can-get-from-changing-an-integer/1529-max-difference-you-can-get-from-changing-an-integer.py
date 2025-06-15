class Solution:
    def maxDiff(self, num: int) -> int:
        ans = 0
        man,mix = '',''
        found = 0
        for i in str(num):
            if i!='9':
                found = i
                break
        fo2 = 0
        f = True
        for i in str(num):
            if f:
                if i!='1':
                    fo2 = i
                    break
                f = False
            else:
                if i!='1' and i!='0':
                    fo2 = i
                    break
        
        for i in str(num):
            if i == found:
                man += '9'
            else:
                man += i
            if i == fo2:
                if fo2 == str(num)[0]:
                    mix += '1'
                else:
                    mix += '0'
            else:
                mix += i
        return int(man)-int(mix)