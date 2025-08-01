"""
Problem: 0080. Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Description:
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
    The relative order of the elements should be kept the same. Return the number of elements left in nums after duplicates are removed.

Approach:
    Use two pointers and a counter to allow at most two occurrences of each element.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates in-place and return the new length (allow at most two occurrences)."""
        if not nums:
            return 0
        write = 1
        count = 1
        for read in range(1, len(nums)):
            if nums[read] == nums[read - 1]:
                count += 1
            else:
                count = 1  # new number, reset count
            if count <= 2:
                nums[write] = nums[read]
                write += 1
        return write

if __name__ == "__main__":
    l = [1,1,1,2,2,2,3]
    sol = Solution()
    k = sol.removeDuplicates(l)
    print(k, l[:k])  # Output: 5 [1, 1, 2, 2, 3]
