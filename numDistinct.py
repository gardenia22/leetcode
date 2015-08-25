class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        if s=="": return 0
        n,m = len(s),len(t)
        # f = [[0 for i in range(n)] for j in range(m)]
        # for i in range(m):
        #     for j in range(i,n):
        #         f[i][j] = f[i][j-1]
        #         if t[i]==s[j]:
        #             if i>0:
        #                 f[i][j] += f[i-1][j-1]
        #             else:
        #                 f[i][j] += 1
        # return f[m-1][n-1]
        for i in range(m):
            f = [0 for j in range(n)]
            for j in range(i,n):
                f[j] = f[j-1]
                if t[i]==s[j]:                   
                    f[j] += g[j-1] if i>0 else 1
            g = f
        return f[n-1]
a = Solution()
print a.numDistinct("ddd","dd")