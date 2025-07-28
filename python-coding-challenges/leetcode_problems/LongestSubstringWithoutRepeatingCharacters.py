
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        check_set = set()
        length = 0
        end = 0
        for start in range(n):

            while end < n and s[end] not in check_set:
                check_set.add(s[end])
                length = max(end + 1 - start, length)
                end += 1
            check_set.remove(s[start])

        return length

sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))