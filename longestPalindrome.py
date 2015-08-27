class Solution:
    # @param {string} s
    # @return {string}

    def longestPalindrome(self, s):
        pass

    def palindrome3(self, s):
        s = "".join(map(lambda x: '_'+x, s))+'_'
        n = len(s)
        ans = 0
        for i in range(n):
            l = r = i
            while l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            ans = max(ans, r-l+1)
        return ans/2

    def palindrome2(self, s):
        n = len(s)
        dp = [[False for i in range(n)]for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            dp[i][i-1] = True
        ans = 0
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans = l
        return ans

    def palindrome1(self, s):
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if j-i+1 > ans and s[i:j] == s[j:i:-1]:
                    ans = j-i+1
        return ans

    def palindrome4(self, s):
        s = "".join(map(lambda x: '_'+x, s))+'_'
        n = len(s)
        length = [0 for i in range(n)]
        c = 0
        ans = 0
        while c < n:
            l = c-length[c]/2
            r = c+length[c]/2
            while l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            length[c] = r-l+1
            if length[c] > ans:
                ans = length[c]
                substring = s[l:r]

            i = 1
            while c-i >= 0 and c+i < n and \
                    c-i-length[c-i]/2 > c-length[c]/2 or \
                    (c-i-length[c-i]/2 == c-length[c]/2 and
                        c+length[c]/2 == n-1):
                length[c+i] = length[c-i]
                i += 1
            if c-i >= 0 and c+i < n and c-i-length[c-i]/2 == c-length[c]/2:
                length[c+i] = length[c-i]

            c = c + i

        return substring.replace("_", "")
a = Solution()
# print a.longestPalindrome("1"*1000)
# print a.palindrome4("ababa")
# print
# a.palindrome4("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print a.palindrome4("kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv")
