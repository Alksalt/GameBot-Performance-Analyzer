class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        # If we're at a leaf node, check if the remaining sum equals node's value
        if not root.left and not root.right:
            return root.val == targetSum

        # Subtract current value from the target and recurse down
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))