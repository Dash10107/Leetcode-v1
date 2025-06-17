class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def func(ind,s,opens=0,close=0):
            if ind>=len(s):
                if opens==close:
                    return [s]
                return []
            if close>opens:
                return []
            delet = []
            if s[ind] in '()':
                new = s.copy()
                del new[ind]
                delet = func(ind,new,opens,close)
            if s[ind]=='(':
                opens+=1
            elif s[ind]==')':
                close+=1
            keeps = func(ind+1,s,opens,close)
            if (not delet) or (not keeps) or (len(delet[0])==len(keeps[0])):
                return delet+keeps
            elif len(delet[0])<len(keeps[0]):
                return keeps
            elif len(delet[0])>len(keeps[0]):
                return delet
        return list(set(''.join(el) for el in func(0,list(s)) ))