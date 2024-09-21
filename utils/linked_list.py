class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def as_linked_list(cls, nodes):
        """Converts an array of nodes in to
        a linked list and returns its head"""
        parent = cls()
        node = parent
        for n in nodes:
            node.next = cls(val=n)
            node = node.next
        return parent.next

    def as_list(self):
        """returns all the nodes after self (inclusive) as an array"""
        ans = []
        head = self
        while head is not None:
            ans.append(head.val)
            head = head.next
        return ans
