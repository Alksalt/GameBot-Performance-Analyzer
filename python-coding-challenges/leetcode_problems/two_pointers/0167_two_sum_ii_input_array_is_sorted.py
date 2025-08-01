"""
Problem: 0167. Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed).

Approach:
Two pointers — start at both ends and move towards each other to find the pair.

Time Complexity:
- Time: O(n)
- Space: O(1)
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1
        return []

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Expected: [1, 2]
