class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip(" ")
        if not s: return False
        return self.isUnsigned(s) or \
               (s[0] in ['-','+'] and self.isUnsigned(s[1:]))

    def isUnsigned(self, s):
        return self.isDigits(s) or self.isDecimal(s) or self.isScientific(s)

    def isDigits(self, s):
        if not s: return False
        for i in s:
            if i not in "0123456789":
                return False
        return True

    def isScientific(self, s):
        pE = s.find("e")
        if pE==-1: 
            return False 
        else:
            before = (self.isDigits(s[:pE]) or self.isDecimal(s[:pE]))
            after = self.isDigits(s[pE+1:]) or (bool(s[pE+1:]) and \
                    s[pE+1] in ['-','+'] and self.isDigits(s[pE+2:]))
            return (before and after)
            

    def isDecimal(self, s):
        pDot = s.find(".")
        if pDot==-1: 
            return False 
        else:
            before = self.isDigits(s[:pDot])
            after = self.isDigits(s[pDot+1:])
            return (before and after) or \
                   (not s[:pDot] and after) or \
                   (before and not s[pDot+1:])

a = Solution()
# print a.isNumber("0")
# print a.isNumber(" 0.1 ")
# print a.isNumber("abc")
# print a.isNumber("1 a")
# print a.isNumber("2e10")
# print a.isNumber(".1e")
print a.isNumber("-7e")