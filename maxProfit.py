class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        i = 0
        ans = 0
        while i<n:
            low = prices[i]
            while i+1<n and prices[i+1]>=prices[i]:
                i += 1
            ans += prices[i]-low
            while i+1<n and prices[i+1]<prices[i]:
                i += 1
            if i==n-1:
                break
        return ans
            
        
a = Solution()
print a.maxProfit([1,2,3,2,1,4,2,4])