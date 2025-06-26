class Solution:
    def maximumBinaryString(self, b: str) -> str:
        f = b.find('0')
        if f==-1:
            return b
        cz = b.count('0',f)
        ans = '1'*f + '1'*(cz-1)+'0'+'1'* (len(b)-f-cz)
        return ans