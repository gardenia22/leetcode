class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        #return sorted(nums)[len(nums)/2]
        count = 0
        for x in nums:
            if count==0:
                ans = x
                count = 1
            else:
                count += 1 if ans==x else -1
        return ans
                
            