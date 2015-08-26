class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator==0: return None
        if numerator==0: return "0"
        sign = 1
        if numerator<0: 
            numerator = -1 * numerator
            sign = -1
        if denominator<0: 
            denominator = -1 * denominator
            sign *= -1
        # integer part of answer
        integer = str(numerator / denominator)
        if sign==-1:
            integer = '-'+integer
        
        # fraction part of answer
        remain = numerator % denominator
        fraction,used,index = "",{},0
        used[remain] = 0

        while remain>0:            
            digit = str(remain*10 / denominator)
            fraction += digit
            remain = remain*10 % denominator            
            if remain in used.keys():
                # if the value of remain appears before
                # then we find the recurring part.
                repeat = used[remain]
                fraction = fraction[:repeat]+'('+fraction[repeat:]+')'
                break
            index += 1
            used[remain] = index

        if fraction!="":
            # if has fraction part
            fraction = '.'+fraction
        return integer+fraction

        # ans = integer + fraction
a = Solution()
print a.fractionToDecimal(20, -13)