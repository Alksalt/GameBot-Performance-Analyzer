"""
Problem: 0209. Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Description:
    Find the minimal length of a contiguous subarray of which the sum is at least target.

Approach:
    Use a sliding window to expand and contract the subarray while tracking the sum.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        sub_sum = 0
        best_length = float('inf')

        for end in range(n):
            sub_sum += nums[end]

            while sub_sum >= target:
                best_length = (end + 1 - start) if (end + 1 - start) < best_length else best_length
                start += 1
                sub_sum -= nums[start - 1]



        return 0 if best_length == float('inf') else best_length


target = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(target,nums))