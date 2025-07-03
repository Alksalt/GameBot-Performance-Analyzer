class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = 'Fuck you idiot   ps sorry'
sol = Solution()
print(sol.lengthOfLastWord(s))
