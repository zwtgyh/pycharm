class Solution():
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
###
a = Solution()
a.isPalindrome(12021)