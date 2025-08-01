"""
Problem: 0100. Same Tree
Link: https://leetcode.com/problems/same-tree/

Description:
    Determine if two binary trees are structurally identical and have the same node values.

Approach:
    Recursively compare nodes and their children for equality.

Time Complexity: O(N)
Space Complexity: O(H)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)