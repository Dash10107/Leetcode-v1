class Solution:
    def reformatDate(self, date: str) -> str:
        
        a=date.split(' ')
        a.reverse()
        monthDict = {'Jan': '01', 'Feb': '02', 
                     'Mar': '03', 'Apr': '04', 
                     'May': '05', 'Jun': '06', 
                     'Jul': '07', 'Aug': '08', 
                     'Sep': '09', 'Oct': '10', 
                     'Nov': '11', 'Dec': '12'}
        if a[1] in monthDict:
            a[1]=monthDict[a[1]]
        a[2]=a[2][:-2]
        if len(a[2])==1:
            a[2]='0'+a[2]
        return a[0]+'-'+a[1]+'-'+a[2]