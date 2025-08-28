class Solution:
    def reformat(self, s: str) -> str:
        alp=0
        num=0
        list1,list2,list3=[],[],[]
        a=len(s)
        for  i in range (0,a):
            # print(s[i].isalpha())
            if s[i].isalpha():
                alp=alp+1
                list1.append(s[i])
                # print(list1)
            else:
                num=num+1
                list2.append(s[i])
                # print(list2)
        # print(alp)
        # print(num)
        if len(list1)!=len(list2):
            if len(list2)-len(list1)==-1 or len(list2)-len(list1)==1:
                if len(list1)>len(list2):
                    i,j = 0,0
                    while i<len(list1) and j<len(list2):
                        list3.append(list1[i])
                        list3.append(list2[j])
                        i+=1;j+=1
                    list3.append(list1[i])
                else:
                    i,j = 0,0
                    while i<len(list1) and j<len(list2):
                        list3.append(list2[j])
                        list3.append(list1[i])
                        i+=1;j+=1
                    list3.append(list2[j]) 
                return ''.join(list3)  
            return ""
        for i in range (0,len(list1)):
            list3.append(list2[i])
            list3.append(list1[i])
        return ''.join(list3)    
        