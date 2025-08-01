"""
Problem: 0503. Next Greater Element II
Link: https://leetcode.com/problems/next-greater-element-ii/

Description:
    For each element in a circular array, find the next greater element.

Approach:
    Use a stack and simulate two passes to handle the circular nature.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in reversed(range(2 * n)):
            idx = i % n

            while stack and nums[stack[-1]] <= nums[idx]:
                stack.pop()

            if stack:
                result[idx] = nums[stack[-1]]

            stack.append(idx)

        return result



nums1 = [1,2,1]    # [1, 0, 2, 1, 0]
nums2 = [1,2,3,4,3]
sol = Solution()
print(sol.nextGreaterElements(nums1))