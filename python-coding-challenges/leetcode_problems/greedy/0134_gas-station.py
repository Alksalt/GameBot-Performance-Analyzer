"""
Problem: 0134. Gas Station
Link: https://leetcode.com/problems/gas-station/

Description:
    Given gas and cost arrays, find the starting gas station index to complete the circuit, or -1 if impossible.

Approach:
    Greedily track total and current gas balance, resetting start when current is negative.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        total, curr, start = 0, 0, 0
        for i in range(n):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        if total < 0:
            return -1
        return start






gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

cases = [
    ([1,2,3,4,5], [3,4,5,1,2]),      # Output: 3
    ([2,3,4], [3,4,3]),              # Output: -1
    ([5,5,5,5], [1,1,1,1]),          # Output: 0
    ([7], [4]),                      # Output: 0
    ([1], [2]),                      # Output: -1
    ([1,3], [2,2]),                  # Output: 1
    ([1,2,1,2], [2,2,2,2]),          # Output: -1
    ([2,3,4], [3,4,2]),              # Output: 2
    ([10000]*10000, [10000]*10000),  # Output: 0
    ([1]*9999+[10000], [2]*9999+[1]) # Output: 9999
]

sol = Solution()
for i, (gas, cost) in enumerate(cases):
    print(f"Test case {i+1}: {sol.canCompleteCircuit(gas, cost)}")


