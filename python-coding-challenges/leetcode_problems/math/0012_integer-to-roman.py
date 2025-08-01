"""
Problem: 0012. Integer to Roman
Link: https://leetcode.com/problems/integer-to-roman/

Description:
    Convert an integer to its Roman numeral representation.

Approach:
    Map values to symbols and subtract largest possible values iteratively.

Time Complexity: O(1)
Space Complexity: O(1)
"""

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