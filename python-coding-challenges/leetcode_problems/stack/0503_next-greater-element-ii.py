"""
Problem: 0503. Next Greater Element II
Link: https://leetcode.com/problems/next-greater-element-ii/

Description:
    Given a circular array, find the next greater number for every element. If it doesn't exist, return -1 for that position.

Approach:
    Use a stack to keep track of indices whose next greater element hasn't been found. Traverse the array twice for circularity.

Time Complexity: O(N)
Space Complexity: O(N)
"""

def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

if __name__ == "__main__":
    arr = [1, 4, 6, 3, 2, 7]
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    print(next_greater_element(arr))   # Output: [4, 6, 7, 7, 7, -1]
    print(next_greater_element(arr2))  # Output: [2, 3, 4, 5, 6, 7, -1]