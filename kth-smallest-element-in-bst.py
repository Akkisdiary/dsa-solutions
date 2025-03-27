# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionBrute:
    def kthSmallest(self, root, k):
        return self.inorder(root)[k-1]

    def inorder(self, root):
        if not root:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    assert SolutionBrute().kthSmallest(root, 3) == 3
