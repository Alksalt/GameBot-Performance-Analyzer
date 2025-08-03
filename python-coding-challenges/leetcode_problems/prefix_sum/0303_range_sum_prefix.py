"""
Problem: 0303. Range Sum Query - Immutable
Link: https://leetcode.com/problems/range-sum-query-immutable/

Description:
Implement a class `NumArray` that efficiently supports the following operation:
    - sumRange(i, j): Return the sum of elements between indices i and j inclusive.

Approach:
Prefix Sum – precompute cumulative sums in __init__ and use them to return results in O(1) time.

Time Complexity:
- __init__: O(n)
- sumRange: O(1)
- Space: O(n)
"""

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left - 1] if left > 0 else self.prefix[right]


# Example usage
if __name__ == "__main__":
    num_array = NumArray([1, 3, 4, 5, 6, 7, 43, 3, 4, 5, 7, 9, 6])
    print(num_array.sumRange(1, 5))  # Output: 25
