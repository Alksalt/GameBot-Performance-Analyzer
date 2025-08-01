"""
Problem: 0045. Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/

Description:
    Given an array of non-negative integers, find the minimum number of jumps to reach the last index.

Approach:
    Use a greedy strategy to track the farthest reachable index and increment jumps when reaching the end of the current range.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        farthest = 0
        jumps = 0
        current_end = 0

        for i in range(n - 1):
            if i > farthest:
                return -1
            farthest = max(farthest, i + nums[i])
            if current_end == i:
                jumps += 1
                current_end = farthest
            if current_end >= n - 1:
                break
        return jumps
