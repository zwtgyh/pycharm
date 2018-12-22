class Solution():
    def reverse(self, x):
        if x == 0:
            return 0;
        elif x < 0:
            sign = -1
        elif x > 0:
            sign = 1
        r = int( str(sign*x)[::-1] )
        return sign*r * (r < 2 ** 31)
class Solution():
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31:
                return 0
            else:
                return int(revst)


#测试
a = Solution()
a.reverse(-123)

# class Solution:
#     def reverse(self, x):
#         if x == 0:
#             return 0
#         else:
#             import operator
#             sign = operator.gt(x, 0)       #此程序错误，因为operator.gt(x,y) 在x<y时，返回0不是返回-1.
#             r = int(str(sign*x)[::-1])
#             return sign*r * (r < 2 ** 31)