class Solution:
    def solveEquation(self, eq: str) -> str:
        left, right = eq.split('=')

        def helper(expr: str):
            coeff = 0
            const = 0
            val = ''
            sign = 1
            i = 0
            while i < len(expr):
                if expr[i] in '+-':
                    sign = 1 if expr[i] == '+' else -1
                    i += 1
                val = ''
                while i < len(expr) and expr[i].isdigit():
                    val += expr[i]
                    i += 1
                if i < len(expr) and expr[i] == 'x':
                    coeff += sign * int(val or '1')
                    i += 1
                else:
                    const += sign * int(val or '0')
            return coeff, const

        lcoeff, lconst = helper(left)
        rcoeff, rconst = helper(right)

        final_coeff = lcoeff - rcoeff
        final_const = rconst - lconst

        if final_coeff == 0:
            if final_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={final_const // final_coeff}"
