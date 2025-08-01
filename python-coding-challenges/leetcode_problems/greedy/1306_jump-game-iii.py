"""
Problem: 1306. Jump Game III
Link: https://leetcode.com/problems/jump-game-iii/

Description:
    Given an array and a start index, determine if you can reach any index with value 0 by jumping left or right.

Approach:
    Use BFS or DFS to explore all reachable indices, marking visited to avoid cycles.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()
        queue = deque([start])
        n = len(arr)
        while queue:
            i = queue.popleft()
            right = i + arr[i]
            left = i - arr[i]
            if i in visited:
                continue
            else:
                visited.add(i)
            if right < n:
                if arr[right] == 0:
                    return True
                queue.append(right)
            if left >= 0:
                if arr[left] == 0:
                    return True
                queue.append(left)
        return False
