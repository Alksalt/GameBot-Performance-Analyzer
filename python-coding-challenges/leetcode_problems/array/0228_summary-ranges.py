"""
Problem: 0228. Summary Ranges
Link: https://leetcode.com/problems/summary-ranges/

Description:
    Given a sorted integer array without duplicates, return the smallest sorted list of ranges that cover all the numbers in the array exactly.
    Each range [a,b] should be output as:
    - "a->b" if a != b
    - "a" if a == b

Approach:
    Iterate through the array, tracking the start of each range and appending ranges to the result list.

Time Complexity: O(N)
Space Complexity: O(1) (excluding output)
"""

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        n = len(nums)
        start = 0
        for i in range(1, n + 1):
            if i == n or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        return result

if __name__ == "__main__":
    n1 = [0, 2, 3, 4, 6, 8, 9]
    n2 = [0, 1]
    n3 = [0, 1, 2, 4, 5, 7]
    n4 = [1]
    n5 = []
    sol = Solution()
    print(sol.summaryRanges(n1))  # Output: ['0', '2->4', '6', '8->9']
    print(sol.summaryRanges(n2))  # Output: ['0->1']
    print(sol.summaryRanges(n3))  # Output: ['0->2', '4->5', '7']
    print(sol.summaryRanges(n4))  # Output: ['1']
    print(sol.summaryRanges(n5))  # Output: []