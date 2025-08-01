"""
Problem: 0066. Plus One
Link: https://leetcode.com/problems/plus-one/

Description:
    Given a non-empty array of digits, increment one to the integer represented by the array.

Approach:
    Traverse from the end, handle carry, and prepend 1 if needed.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

i = [9, 9, 9, 9, 9, 9]

o = 15 % 10
s = Solution()
print(s.plusOne(i))