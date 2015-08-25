class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ans = 0
        while n!=0:
            if n%2==1:
                ans += 1
            n = n/2
        return ans
a = Solution()
print a.hammingWeight(11)