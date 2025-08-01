"""
Problem: 0496. Next Greater Element I
Link: https://leetcode.com/problems/next-greater-element-i/

Description:
    For each element in nums1, find the next greater element in nums2.

Approach:
    Use a stack to build a mapping from each number to its next greater element in nums2.

Time Complexity: O(N + M)
Space Complexity: O(N)
"""

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        result = [-1] * len(nums1)
        next_greater = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                next_greater[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)

        for j in range(len(nums1)):
            if nums1[j] in next_greater:
                result[j] = next_greater[nums1[j]]

        return result
nums1 = [4,1,2]
nums2 = [1,3,4,2]



sol = Solution()
print(sol.nextGreaterElement(nums1,nums2))