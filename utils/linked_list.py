class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __as_string(self):
        seen = []
        arr = []
        node = self
        while node:
            if node in seen:
                arr.append(f"({node.val})")
                break
            seen.append(node)
            arr.append(node.val)
            node = node.next
        return " -> ".join(map(str, arr))

    def __str__(self) -> str:
        return self.__as_string()

    def __repr__(self) -> str:
        return self.__as_string()

    @classmethod
    def as_linked_list(cls, nodes, pos=-1):
        """Converts an array of nodes into a linked list
        and returns it's head. if pos is given, point last node
        to the node at `pos` creating a cycle in it"""
        memo = []
        parent = cls()
        node = parent
        for n in nodes:
            node.next = cls(val=n)
            node = node.next
            memo.append(node)
        if pos >= 0:
            memo[-1].next = memo[pos]
        return parent.next

    def as_list(self):
        """returns all the nodes after self (inclusive) as an array"""
        ans = []
        head = self
        while head is not None:
            if head in ans:
                break
            ans.append(head.val)
            head = head.next
        return ans
