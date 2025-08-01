"""
Problem: 2834. Find the Minimum Possible Value After Modification
Link: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

Description:
    Given an array nums, find the smallest missing integer greater than the sum of the longest prefix of consecutive integers starting from nums[0].

Approach:
    Find the sum of the longest prefix of consecutive numbers, then increment until you find a missing integer.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        seq_sum = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        seq_set = set(nums)
        while seq_sum in seq_set:
            seq_sum += 1
        return seq_sum

if __name__ == "__main__":
    nums = [3, 4, 5, 1, 12, 14, 13]
    n = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.missingInteger(nums))  # Output: 6
    print(sol.missingInteger(n))     # Output: 6