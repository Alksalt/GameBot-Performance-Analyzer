"""
Problem: 0231. Power of Two
Link: https://leetcode.com/problems/power-of-two/

Description:
    Determine if an integer is a power of two using iterative, recursive, or bitwise methods.

Approach:
    Divide by 2, use recursion, or check n & (n-1) == 0 for n > 0.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

from collections import Counter
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True

        while n > 1:
            n = n / 2
        if n == 1:
            return True
        else:
            return False
    def isPowerOfTwo_rec(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True

        return self.isPowerOfTwo(n=n/2)
    def isPowerOfTwo_sec(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


n = 6
sol = Solution()
print(sol.isPowerOfTwo_rec(n))