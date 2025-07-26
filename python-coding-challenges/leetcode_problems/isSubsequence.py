class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            return False
        if not s:
            return True
        i = j = 0

        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if i == len(s):
                return True

        return False