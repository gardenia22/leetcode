class Solution:
    # @param {integer} n
    # @return {string}

    def convertToTitle(self, n):
        ans = ''
        while n > 0:
            if n % 26:
                ans = chr(n % 26+64) + ans
                n /= 26
            else:
                ans = 'Z' + ans
                n = n/26-1
        return ans
