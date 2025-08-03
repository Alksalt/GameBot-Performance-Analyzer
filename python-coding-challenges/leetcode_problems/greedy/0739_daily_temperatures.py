"""
Problem: 0739. Daily Temperatures
Link: https://leetcode.com/problems/daily-temperatures/

Description:
Given a list of daily temperatures, return a list such that for each day,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for that, put 0 instead.

Approach:
Monotonic Stack – store indices of unresolved days in decreasing order of temperature.
For each temperature, pop all indices from the stack with smaller temperatures and compute the wait.

Time Complexity:
- Time: O(n)
- Space: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []  # Stores indices
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result


# Example usage
if __name__ == "__main__":
    s = Solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temps))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
