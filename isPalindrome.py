import math


class Solution:
    # @param {integer} x
    # @return {boolean}

    def isPalindrome(self, x):
        if x < 0:
            return False
        y = 0
        z = x
        while z > 0:
            y = y*10 + z % 10
            z = z/10
        return x == y
a = Solution()
print a.isPalindrome(11)
