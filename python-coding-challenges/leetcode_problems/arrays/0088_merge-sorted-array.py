"""
Problem: 0088. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/

Description:
    Merge two sorted integer arrays nums1 and nums2 into nums1 as one sorted array in-place.

Approach:
    Use two pointers from the end to fill nums1 from the back.

Time Complexity: O(M + N)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i1 = m - 1
        i2 = n - 1
        k = m + n - 1
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[k] = nums1[i1]
                i1 -= 1
            else:
                nums1[k] = nums2[i2]
                i2 -= 1
            k -= 1
l1 = [1,2,3,0,0,0]
m = 3
l2 = [2,5,7]
n = 3

s = Solution()
s.merge(l1,3,l2,3)
print(l1)

