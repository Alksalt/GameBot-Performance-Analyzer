
"""
Problem: 0026. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Description:
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same. Return the number of unique elements in nums.

Approach:
    Use two pointers: one for writing unique elements, one for scanning the array.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates in-place and return the new length (allow only one occurrence)."""
        if not nums:
            return 0
        write = 1
        scan = 0
        for read in range(1, len(nums)):
            if nums[scan] == nums[read]:
                continue
            else:
                nums[write] = nums[read]
                scan = read
                write += 1
        return write

if __name__ == "__main__":
    l = [1, 1, 2, 2, 3]
    sol = Solution()
    k = sol.removeDuplicates(l)
    print(k, l[:k])  # Output: 3 [1, 2, 3]
