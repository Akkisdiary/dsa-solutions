# 101. Symmetric Tree - https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"<TreeNode [{self.val}]>"

    def __str__(self) -> str:
        return str(self.val)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.equals([root.left], [root.right])

    def equals(self, left, right):
        """
        :type left: List[TreeNode]
        :type right: List[TreeNode]
        :rtype: bool
        """
        if len(left) == len(right) == 0:
            return True

        if len(left) != len(right):
            return False

        left_subtrees = []
        right_subtrees = []
        n = len(left)
        for l_idx in range(n):
            r_idx = n - l_idx - 1

            if left[l_idx] is not None:
                left_subtrees.append(left[l_idx].left)
                left_subtrees.append(left[l_idx].right)
            if right[l_idx] is not None:
                right_subtrees.append(right[l_idx].left)
                right_subtrees.append(right[l_idx].right)

            if left[l_idx] is None and right[r_idx] is None:
                continue
            if left[l_idx] is None or right[r_idx] is None:
                return False
            if left[l_idx].val != right[r_idx].val:
                return False

        return self.equals(left_subtrees, right_subtrees)


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


tree = to_binary_tree([1, 2, 2, None, 3, 3])
print(Solution().isSymmetric(tree))
