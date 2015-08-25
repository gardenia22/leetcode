class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}

    def combinationSum3(self, k, n):
        self.prev = []
        self.ans = []
        self.search(k,n)
        return self.ans

    def search(self, k, n):
        if k==0 and n==0:
            self.ans.append(list(self.prev))
        if k==0 or n==0:
            return 0
        for x in range(1,10):
            if (len(self.prev)==0 or x > self.prev[-1]) and x<=n:
                self.prev.append(x)
                self.search(k-1,n-x)
                self.prev.remove(x)

a = Solution()
print a.combinationSum3(3,9)
        