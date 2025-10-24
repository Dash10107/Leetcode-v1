class Solution:
    def distMoney(self, money: int, children: int) -> int:
        rem  = money-children
        if rem<0:return -1
        seven = rem//7
        mod = rem%7
        if seven<children:
            space = children-seven
            if mod==3 and space==1:return max(seven-1,0)
            else:return seven
        elif seven>children:
            return children-1
        else:
            if mod==0:return seven
            else:return max(0,seven-1)
        