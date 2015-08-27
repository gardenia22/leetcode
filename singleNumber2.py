class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for x in nums:
            one, two = (one & ~x) | (x & ~one & ~two), (one & x) | (two & ~x)
        return one

print Solution().singleNumber([1, 1, 1, 2])
