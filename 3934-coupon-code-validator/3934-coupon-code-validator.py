class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        b = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        n = len(code)
        valid = []
        for i in range(n):
            if  isActive[i] and bool(re.fullmatch(r'[a-zA-Z0-9_]+', code[i])) and businessLine[i] in b:
                valid.append((b[businessLine[i]],code[i]))
        valid.sort()
        return [c for _,c in valid]