class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

s = "   fly me   to   the moon  "
s2 = "luffy is still joyboy"
sol = Solution()
print(sol.lengthOfLastWord(s2))