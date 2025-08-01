"""
Problem: 0189. Rotate Array
Link: https://leetcode.com/problems/rotate-array/

Description:
    Given an array, rotate the array to the right by k steps, where k is non-negative.

Approach:
    Several approaches shown:
    - Reverse the whole array, then reverse each part.
    - Use slicing to move the tail to the front.

Time Complexity: O(N)
Space Complexity: O(1) for in-place, O(N) for slicing.
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """Reverse approach: rotate array to the right by k steps in-place."""
        n = len(nums)
        k = k % n
        nums.reverse()
        i1, i2 = 0, k - 1
        while i1 < i2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i1 += 1
            i2 -= 1
        i1, i2 = k, n - 1
        while i1 < i2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i1 += 1
            i2 -= 1

    def rotate2(self, nums: list[int], k: int) -> None:
        """Slicing approach: rotate array to the right by k steps using extra space."""
        n = len(nums)
        k %= n
        if k == 0:
            return
        tail = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = tail

    def rotate3(self, nums: list[int], k: int) -> None:
        """Alternative slicing approach."""
        n = len(nums)
        k %= n
        if k == 0:
            return
        tail = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = tail

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol = Solution()
    arr = nums.copy()
    sol.rotate(arr, k)
    print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
    arr = nums.copy()
    sol.rotate2(arr, k)
    print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
    arr = nums.copy()
    sol.rotate3(arr, k)
    print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]

