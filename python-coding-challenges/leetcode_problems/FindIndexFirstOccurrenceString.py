class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i1 = i2 = 0
        n = len(needle)
        while i1 < len(haystack):
            if haystack[i1] == needle[i2]:
                i1 += 1
                i2 += 1
                if i2 == n:
                    return i1 - i2
            else:
                i1 = i1 + 1 - i2
                i2 = 0
        return -1

haystack = "mississippi"
needle = "issip"

s = Solution()
print(s.strStr(haystack,needle))