# 61. Rotate List
# https://leetcode.com/problems/rotate-list/description/

from utils import ListNode, TestRunner


class Solution:
    def rotateRight(self, head, k):
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        ans = node = head
        if length > 1:
            k = k % length
            if k > 0:
                while node and node.next:
                    if length == k + 1:
                        tmp = node.next
                        node.next = None
                        node = ans = tmp
                    else:
                        node = node.next
                    length -= 1
                node.next = head
        return ans


test_cases = [
    {
        "input": {"head": ListNode.as_linked_list([1, 2, 3, 4, 5]), "k": 2},
        "expected": ListNode.as_linked_list([4, 5, 1, 2, 3]),
    },
    {
        "input": {"head": ListNode.as_linked_list([0, 1, 2]), "k": 4},
        "expected": ListNode.as_linked_list([2, 0, 1]),
    },
    {
        "input": {"head": ListNode.as_linked_list([]), "k": 0},
        "expected": ListNode.as_linked_list([]),
    },
    {
        "input": {"head": ListNode.as_linked_list([1]), "k": 1},
        "expected": ListNode.as_linked_list([1]),
    },
    {
        "input": {"head": ListNode.as_linked_list([1, 2]), "k": 0},
        "expected": ListNode.as_linked_list([1, 2]),
    },
]

if __name__ == "__main__":
    TestRunner(Solution().rotateRight, test_cases).test(lambda x: x.as_list() if x else None)
