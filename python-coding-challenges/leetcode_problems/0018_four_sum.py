"""
Problem: 0018. 4Sum
Link: https://leetcode.com/problems/4sum/

Description:
Given an integer array nums and an integer target, return all unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:
    - a, b, c, and d are distinct indices
    - nums[a] + nums[b] + nums[c] + nums[d] == target

Approach:
Sort the array, use two fixed pointers and two pointers (`left`, `right`) to find unique quadruplets that sum to target.

Time Complexity:
- Time: O(n^3)
- Space: O(1) (ignoring output list)
"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for first in range(n - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                left = second + 1
                right = n - 1

                while left < right:
                    current = nums[first] + nums[second] + nums[left] + nums[right]
                    if current == target:
                        result.append([nums[first], nums[second], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current < target:
                        left += 1
                    else:
                        right -= 1

        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 1, -2, 1, 2, 3, 4, 4, -4, 4], 6))
