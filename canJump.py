class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        far = 0
        for i in range(n):
            if i<=far:
                far = max(far,i+nums[i])
            else:
                return False
        return far>=n-1

print Solution().canJump([2,3,1,1,4])