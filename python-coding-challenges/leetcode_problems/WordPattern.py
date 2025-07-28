class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if len(s_list) != len(pattern):
            return False

        d1 = {}
        d2 = {}
        for i in range(len(s_list)):
            if s_list[i] not in d1:
                d1[s_list[i]] = 1
            else:
                d1[s_list[i]] += 1

            if pattern[i] not in d2:
                d2[pattern[i]] = 1
            else:
                d2[pattern[i]] += 1

            if d1[s_list[i]] != d2[pattern[i]]:
                return False
        return True

pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
print(sol.wordPattern(pattern,s))
