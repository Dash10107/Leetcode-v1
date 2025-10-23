class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n <= 2:
            return s[0] == s[1]
        
        pascal = n - 1  
        diff = (int(s[0]) - int(s[n - 1])) % 10
        
        rem, count2, count5 = 1, 0, 0
        
        inverse = {1: 1, 3: 7, 7: 3, 9: 9}
        
        def factorize(x: int):
            count2 = count5 = 0
            while x % 2 == 0:
                count2 += 1
                x //= 2
            while x % 5 == 0:
                count5 += 1
                x //= 5
            return x % 10, count2, count5
        
        for i in range(1, pascal):
            num = pascal - i      
            den = i          
            
            r_num, cnt2_num, cnt5_num = factorize(num)
            r_den, cnt2_den, cnt5_den = factorize(den)
            
            rem = (rem * r_num * inverse[r_den]) % 10
            count2 = count2 + cnt2_num - cnt2_den
            count5 = count5 + cnt5_num - cnt5_den
            
            if count2 > 0 and count5 > 0:
                c = 0
            elif count2 > 0:
                power = [6, 2, 4, 8] 
                two_mod = power[count2 % 4] if count2 % 4 != 0 else 6
                c = (rem * two_mod) % 10
            elif count5 > 0:
                c = (rem * 5) % 10
            else:
                c = rem
            
            diff = (diff + (int(s[i]) - int(s[n - 1 - i])) * c) % 10
        
        return diff % 10 == 0