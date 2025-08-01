"""
Problem: 0219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/

Description:
    Given an array and integer k, check if any value appears at least twice within k indices.

Approach:
    Use a hash map to track indices of seen values and compare distances.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d_with_idx = {}
        for i, num in enumerate(nums):
            if num in d_with_idx and i - d_with_idx[num] <= k:
                return True
            d_with_idx[num] = i
        return False


nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums,k))