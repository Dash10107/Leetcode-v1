class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op.startswith('-'):
                s = int(op[1:])
                st.append(-s)
            if op.isdigit():
                st.append(int(op))
            elif op=='+':
                st.append(st[-1]+st[-2])
            elif op=='C':
                st.pop()
            elif op=='D':
                st.append(st[-1]*2)
        return sum(st)