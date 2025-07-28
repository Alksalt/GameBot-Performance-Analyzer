from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magasine_dict = Counter(magazine)
        for item, val in ransom_dict.items():
            if val > magasine_dict.get(item, 0):
                return False
        return True

    from collections import Counter
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)

sol = Solution()

# Examples
print(sol.canConstruct("a", "b"))  # False ('a' not in magazine)
print(sol.canConstruct("aa", "ab"))  # False (only one 'a' in magazine)
print(sol.canConstruct("aa", "aab"))  # True  (two 'a's in magazine)