class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        count ={}
        for i in range(len(s)):
            key = s[i:i+10]
            count[key] = count.get(key,0) + 1
        ans = []
        for key in count:
            if count[key] > 1:
                ans.append(key)
        return ans
        
# a = Solution()
# print a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")