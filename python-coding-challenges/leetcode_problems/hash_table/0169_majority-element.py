"""
Problem: 0169. Majority Element
Link: https://leetcode.com/problems/majority-element/

Description:
    Find the element that appears more than ⌊n/2⌋ times in an array.

Approach:
    Use a hash map to count occurrences and return the majority element.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums) // 2
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else: d[i] += 1

            if d[i] > n:
                return i



sol = Solution()
print(sol.majorityElement([1,2,1,2,3,2]))