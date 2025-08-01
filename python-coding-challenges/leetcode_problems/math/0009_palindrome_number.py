"""
Problem: 0009. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Description:
Given an integer `x`, return `True` if it is a palindrome, and `False` otherwise.
A palindrome is a number that reads the same backward as forward.

Approach:
1. Math approach – compare digits from both ends without converting to string.
2. String approach – convert to string and compare characters from both sides.

Time Complexity:
- Time: O(n) where n is the number of digits
- Space:
  - Math version: O(1)
  - String version: O(n)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        count = 1 if x == 0 else 0
        n = x
        while n > 0:
            count += 1
            n //= 10

        value = 10 ** (count - 1)
        while x // 10 != 0:
            right = x // value
            left = x % 10

            if right != left:
                return False

            x = (x % value) // 10
            value //= 100

        return True

    def isPalindrome2(self, x: int) -> bool:
        # String-based solution
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # Expected: True
    print(sol.isPalindrome(-121))  # Expected: False
    print(sol.isPalindrome(10))    # Expected: False
