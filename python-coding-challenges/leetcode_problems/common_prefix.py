class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:

            i = 0

            while i < len(word) and i < len(prefix) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]

            if not prefix:
                return ""

        return prefix



strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))