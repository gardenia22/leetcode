class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        for x in count:
            if count[x]>1:
                return True
        return False