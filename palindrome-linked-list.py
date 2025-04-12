# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/editorial/


from utils import TestRunner, ListNode


class SolutionBrute:
    def isPalindrome(self, head):
        reversed = self.reverse(head)
        while head and reversed:
            if head.val != reversed.val:
                return False
            head = head.next
            reversed = reversed.next
        return True

    def reverse(self, head):
        head = self.copy(head)
        if not head:
            return head
        prev = None
        while head.next:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head.next = prev
        return head

    def copy(self, head):
        d = ListNode()
        node = d
        while head:
            node.next = ListNode(val=head.val)
            node = node.next
            head = head.next
        return d.next


class SolutionBetter:
    def isPalindrome(self, head):
        length = self.length(head)
        stack = []
        i = 0
        while head:
            if length % 2 == 1 and i == length // 2:
                pass
            elif i < length // 2:
                stack.append(head.val)
            elif stack[-1] != head.val:
                return False
            else:
                stack.pop(-1)
            head = head.next
            i += 1
        return len(stack) == 0

    def length(self, head, s=0):
        if head:
            return self.length(head.next, s + 1)
        return s


class SolutionOptimal:
    def isPalindrome(self, head):
        if head:
            d = ListNode(next=head)
            mid = self.find_mid(head)
            rev = self.reverse(mid.next)

            i = d.next
            j = rev
            while j:
                if i.val != j.val:
                    return False
                i = i.next
                j = j.next
        return True

    def find_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        def solve(h, p):
            if not h:
                return p
            nxt = h.next
            h.next = p
            return solve(nxt, h)

        return solve(head, None)


cases = [
    {
        "input": {"head": ListNode.as_linked_list([1, 2, 2, 1])},
        "expected": True,
    },
    {"input": {"head": ListNode.as_linked_list([1, 2])}, "expected": False},
    {"input": {"head": ListNode.as_linked_list([])}, "expected": True},
    {
        "input": {"head": ListNode.as_linked_list([3, 2, 3, 2, 3])},
        "expected": True,
    },
    {
        "input": {"head": ListNode.as_linked_list([3, 2, 1, 3, 2, 3])},
        "expected": False,
    },
    {
        "input": {"head": ListNode.as_linked_list([12, 3, 4, 5, 6])},
        "expected": False,
    },
    {
        "input": {"head": ListNode.as_linked_list([1, 2, 2, 3, 3, 1])},
        "expected": False,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().isPalindrome).test(cases)
