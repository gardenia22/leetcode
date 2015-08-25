class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num<=0: return False
        while num!=1:
            flag = True
            for d in [2,3,5]:
                if num%d == 0:
                    num /= d
                    flag = False
            if flag: return False
        return True
                