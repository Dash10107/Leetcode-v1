class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vow,con = False,False
        vowels = 'aeiou';cons = 'bcdfghjklmnopqrstvwxyz'
        for ch in word:
            if  ch.lower() in vowels :
                vow=True
            elif  ch.lower() in cons:
                con =True
            elif ch in '0123456789':
                continue
            else:
                return False
        if con and vow:
            return True
        return False