class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __as_string(self):
        arr = []
        node = self
        while node:
            arr.append(node.val)
            node = node.next
        return " -> ".join(map(str, arr))

    def __str__(self) -> str:
        return self.__as_string()

    def __repr__(self) -> str:
        return self.__as_string()

    @classmethod
    def as_linked_list(cls, nodes):
        """Converts an array of nodes into a linked list
        and returns it's head"""
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
