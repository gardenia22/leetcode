class Solution:
    # @param {string} s
    # @return {integer}

    def titleToNumber(self, s):
        numbers = map(lambda x: ord(x)-ord('A')+1, s)
        return reduce(lambda x, y: x*26+y, numbers)
