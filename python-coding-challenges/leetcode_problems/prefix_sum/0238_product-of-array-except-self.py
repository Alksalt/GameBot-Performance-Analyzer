
"""
Problem: 0238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Description:
    Given an array, return an array where each element is the product of all other elements except itself.

Approach:
    Use prefix and suffix products to compute the result in O(N) time and O(1) extra space.

Time Complexity: O(N)
Space Complexity: O(1) (excluding output)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


nums = [1,2,3,4]
Output = [24,12,8,6]
sol = Solution()
print(sol.productExceptSelf(nums))
