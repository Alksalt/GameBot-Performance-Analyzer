ar = [1,4,6,7,8,9,10,11,14,16]
target = 1
s = Solution()
"""
Problem: 0035. Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/

Description:
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

Approach:
    Use binary search to find the target or the insert position.

Time Complexity: O(log N)
Space Complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """Return the index of target or the insert position using binary search."""
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left

if __name__ == "__main__":
    ar = [1, 4, 6, 7, 8, 9, 10, 11, 14, 16]
    target = 1
    sol = Solution()
    print(sol.searchInsert(ar, target))  # Output: 0