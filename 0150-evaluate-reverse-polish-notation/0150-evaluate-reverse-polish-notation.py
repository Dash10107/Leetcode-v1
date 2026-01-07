class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(tok,a,b):
            if tok=='+':
                return a + b
            elif tok=='-':
                return a-b
            elif tok=='*':
                return a*b
            else:
                return int(a/b)
        st = []
        for tok in tokens:
            if tok in '+-/*':
                temp1 = st.pop()
                temp2 = st.pop()
                st.append(calc(tok,temp2,temp1))
            else:
                st.append(int(tok))
        return st[-1]