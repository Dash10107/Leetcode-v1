class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        curr = ''
        for b in bits:
            curr+=str(b)
            if curr=='11':
                curr=''
            elif curr=='10':
                curr=''
            elif curr=='01':
                curr='1'
            elif curr=='00':
                curr='0'
        return len(curr)!=0