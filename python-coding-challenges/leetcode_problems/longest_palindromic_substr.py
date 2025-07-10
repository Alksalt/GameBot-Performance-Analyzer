class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0
        if n % 2 == 0:
            r = n // 2
            l = r - 1

        else:
            l = n // 2
            r = l
        while l >= 0 and r <= (n - 1) :
            if s[l] == s[r]:
                start = l
                end = r
                l -= 1
                r += 1
            else:


        return s[start:end + 1]



s = 'babad'
sol = Solution()
print(sol.longestPalindrome(s))