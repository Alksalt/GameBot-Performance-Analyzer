"""
Problem: 0001. Two Sum
Link: https://leetcode.com/problems/two-sum/

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution.

Approach:
Use a dictionary to store previously seen numbers and their indices. For each number, check if its complement exists.

Time Complexity:
- Time: O(n)
- Space: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            part = target - num
            if part in seen:
                return [seen[part], i]
            seen[num] = i
        return []

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]

