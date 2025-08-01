"""
Problem: 0027. Remove Element
Link: https://leetcode.com/problems/remove-element/

Description:
    Given an integer array nums and an integer val, remove all occurrences of val in-place and return the new length.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Approach:
    Use two pointers to overwrite elements equal to val. Several variations are shown below.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """Overwrite elements equal to val from the end. Returns new length and modified list."""
        k = len(nums) - 1
        current = k
        while k >= 0:
            if nums[k] == val:
                if k == current:
                    nums[k] = "_"
                    k -= 1
                    current -= 1
                    continue
                nums[k] = nums[current]
                nums[current] = "_"
                k -= 1
                current -= 1
            else:
                k -= 1
        return current + 1, nums

    def removeElement_two_pointer(self, nums: list[int], val: int) -> int:
        """Two-pointer approach from both ends. Returns new length and modified list."""
        end = len(nums) - 1
        start = 0
        while start <= end:
            if nums[end] == val:
                nums[end] = "_"
                end -= 1
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = '_'
                start += 1
                end -= 1
            else:
                start += 1
        return start, nums

    def third(self, nums: list[int], val: int) -> int:
        """Copy non-val elements to a new list. Returns new length and new list."""
        n = len(nums)
        new = [None] * n
        i1 = i2 = 0
        while i1 < n:
            if nums[i1] == val:
                i1 += 1
            else:
                new[i2] = nums[i1]
                i1 += 1
                i2 += 1
        return i2, new

    def forth(self, nums: list[int], val: int) -> int:
        """Overwrite non-val elements in-place. Returns new length."""
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write

if __name__ == "__main__":
    l = [3,2,2,3,4,5,5,2,1,3]
    val = 3
    sol = Solution()
    # Example usage
    print(sol.removeElement(l.copy(), val))
    print(sol.removeElement_two_pointer(l.copy(), val))
    print(sol.third(l.copy(), val))
    print(sol.forth(l.copy(), val))