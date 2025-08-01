"""
Problem: 0202. Happy Number
Link: https://leetcode.com/problems/happy-number/

Description:
    Determine if a number is happy by repeatedly replacing it with the sum of the squares of its digits.

Approach:
    Use a set to detect cycles and iterate until reaching 1 or a loop.

Time Complexity: O(log N)
Space Complexity: O(log N)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        d = {i: i**2 for i in range(10)}
        limit = 1000
        counter = 0
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            current = 0
            right, left = n, 0
            while right not in d:
                right, left = divmod(right, 10)
                current += d[left]
            current += d[right]
            counter += 1
            n = current

            if counter >= limit:
                break


        return n == 1


"""12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1"""
n = 19
sol = Solution()
print(sol.isHappy(n))