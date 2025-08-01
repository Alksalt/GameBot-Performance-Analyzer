"""
Problem: 0101. Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/

Description:
    Check if a binary tree is symmetric around its center.

Approach:
    Recursively compare left and right subtrees for mirror symmetry.

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
    def isSymmetric(self, root) -> bool:
        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False

            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root.left, root.right)


