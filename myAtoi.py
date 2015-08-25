class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        INT_MAX = 2147483647
        # match = re.match(r"([+-])?(\d+)(.0+)?(e(\d+))?",str)
        match = re.match(r"([+-])?(\d+)",str)
        if match:
            baseStr = match.group(2)
            # print baseStr
            baseInt = 0
            for digit in baseStr:
                baseInt = baseInt*10+ord(digit)-ord('0')
            # expStr = match.group(5)
            # expInt = 0
            # if expStr:
            #     for digit in expStr:
            #       expInt += expInt*10+ord(digit)-ord('0')
            #       if expInt>10:
            #         baseInt = INT_MAX
            # print baseInt,expInt
            # i = 0
            # while i<expInt:
            #     # print baseInt
            #     if baseInt >= INT_MAX+1 or baseInt<0:
            #         baseInt = INT_MAX+1
            #         break
            #     baseInt *= 10
            #     i += 1
            if match.group(1)=='-':
                baseInt = min(baseInt,INT_MAX+1)
                baseInt = -baseInt
            else:
                baseInt = min(baseInt,INT_MAX)
            return baseInt
        else:
            return 0