# kth-largest-sum-in-a-binary-tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

from utils import TestRunner


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSums = []
        queue = [root]
        while queue:
            s = 0
            newQueue = []
            for node in queue:
                s += node.val
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            levelSums.append(s)
            queue = newQueue
        levelSums.sort(reverse=True)
        if k - 1 > len(levelSums) - 1:
            return -1
        return levelSums[k-1]


cases = [
    {
        "input": {
            "root": [5,8,9,2,1,3,7,4,6],
            "k": 2,
        },
        "expected": 13
    },
    {
      "input": {
          "root": [1,2,None,3],
          "k": 1,
      },
      "expected": 3
    },
    {
      "input": {
          "root": [5,8,9,2,1,3,7],
          "k": 4,
      },
      "expected": -1
    }
]

# TODO: Figure out tests
