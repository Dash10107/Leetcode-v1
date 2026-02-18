class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st  = [defaultdict(int)]
        i = 0;n=len(formula)
        while i<n:
            if formula[i]=='(':
                st.append(defaultdict(int))
            elif formula[i]==')':
                curr = st.pop()
                count=''
                while i+1<n and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                count = 1 if not count else int(count)
                prev = st[-1]
                for ele in curr:
                    prev[ele]+= curr[ele]*count                    
            else:
                start = i
                count = ''
                while i+1<n and formula[i+1].islower():
                    i+=1
                ele = formula[start:i+1]
                while i+1<n and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                count = 1 if not count else int(count)
                curr = st[-1]
                curr[ele]+=count
            i+=1
        ans = '';last = st[-1]
        for key in sorted(last.keys()):
            count = '' if last[key]==1 else last[key]
            ans += key+str(count)
        return ans
        
