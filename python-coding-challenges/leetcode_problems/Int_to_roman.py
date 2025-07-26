class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        return
num = 3749

Output = "MMMDCCXLIX"
sol = Solution()
print(sol.intToRoman(num))