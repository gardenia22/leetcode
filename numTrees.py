class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        f = [1,1]+[0 for i in range(n-1)]
        for i in range(2,n+1):
            for j in range(1,i+1):
                f[i] += f[j-1]*f[i-j]
        return f[n]

a = Solution()
print a.numTrees(4)