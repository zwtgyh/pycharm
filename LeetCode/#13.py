class Solution():
    def romanToInt(self, s):
        D = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        x = list(s)
        value, i = 0, 0
        while i < len(s):
            if (i+1 < len(s)) and (D[x[i]] < D[x[i+1]]):
                value += (D[x[i+1]] - D[x[i]])
                i += 2
            else:
                value += D[x[i]]
                i += 1
        return value

##
a = Solution()
a.romanToInt('MCMXCIV')