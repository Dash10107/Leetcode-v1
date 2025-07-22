class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(t);n=len(s)
        tmap = Counter(t)
        i=0;j=0;c=m;mi=0;me=float('inf')
        while j<n:
            if tmap[s[j]]>0:
                c-=1
            tmap[s[j]]-=1
            j+=1
            while c==0:
                if (j-i)<me:
                    mi = i
                    me = j-i
                tmap[s[i]]+=1
                if tmap[s[i]]>0:
                    c+=1
                i+=1
        return '' if me==float('inf') else s[mi:mi+me]