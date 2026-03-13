class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        stc = []
        for i in s:
            if i in brackets:
                stc.append(i)
            elif len(stc)==0 or brackets[stc.pop()] != i:
                return False
        return len(stc) == 0