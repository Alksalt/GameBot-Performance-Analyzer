"""
Problem: 0020. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Description:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    - Open brackets are closed by the same type of brackets.
    - Open brackets are closed in the correct order.

Approach:
Use a stack to track opening brackets. For each closing bracket, check for a matching opener.

Time Complexity:
- Time: O(n)
- Space: O(n)
"""

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        d = {')': '(', '}': '{', ']': '['}
        for el in s:
            if el in d.values():
                stack.append(el)
            elif el in d:
                if not stack or stack.pop() != d[el]:
                    return False
            else:
                return False
        return not stack

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))     # Expected: True
    print(sol.isValid("()[]{}")) # Expected: True
    print(sol.isValid("(]"))     # Expected: False
