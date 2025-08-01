"""
Problem: 0128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Description:
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Approach:
    Use a set for O(1) lookups and expand from sequence starts; alternative: sort and group.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import defaultdict
class Solution:
    def longestConsecutive2(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        d = defaultdict(set)
        key = 0
        d[key].add(nums[0])

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                if nums[i] != nums[i - 1]:
                    d[key].add(nums[i])
            else:
                key += 1
                d[key].add(nums[i])
        return len(max(d.values()))

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in nums:
                current = num
                streak = 1
                while current + 1 in nums:
                    current += 1
                    streak += 1
                max_length = max(max_length, streak)

        return max_length



# Example inputs
nums1 = [100, 4, 200, 1, 3, 2]        # Expected: 4 (sequence: 1,2,3,4)
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] # Expected: 9 (sequence: 0,1,2,3,4,5,6,7,8)
nums3 = []                             # Expected: 0
nums4 = [1, 2, 0, 1]                   # Expected: 3 (sequence: 0,1,2)
nums5 = [1,2,3,4,10,11,12]
# Usage example
sol = Solution()
print(sol.longestConsecutive(nums1))  # 4
print(sol.longestConsecutive(nums2))  # 9
print(sol.longestConsecutive(nums3))  # 0
print(sol.longestConsecutive(nums4))  # 3

