class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h = n = 0

        while h <= len(haystack) - 1 :
            if haystack[h] == needle[n]:
                h += 1
                n += 1
            else:
                h = h - n + 1
                n = 0

            if len(needle) == n:
                return h - n

        return -1


haystack = "sadbutsad"
needle = "sad"
sol = Solution()
print(sol.strStr(haystack,needle))