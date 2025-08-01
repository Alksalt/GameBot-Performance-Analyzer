"""
Problem: 0055. Jump Game
Link: https://leetcode.com/problems/jump-game/

Description:
    Given an array of non-negative integers, determine if you can reach the last index starting from the first.

Approach:
    Use greedy strategies to track the farthest reachable index.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """Greedy: jump to the farthest possible index each time."""
        if not nums:
            return False
        n = len(nums)
        i = 0
        while i < n - 1:
            i = i + nums[i]
            if i > n - 1 or ((i < n - 1) and (nums[i] == 0)):
                return False
        return True

    def canJump2(self, nums: list[int]) -> bool:
        """Greedy: track max reachable index as you iterate."""
        if not nums:
            return False
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True
