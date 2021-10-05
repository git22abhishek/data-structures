class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = [str(node.data) for node in self]
        return ' -> '.join(nodes)

    def insert_at_head(self, data):
        if self.head is not None:
            new_node = Node(data, self.head)
            self.head = new_node
        else:
            self.head = Node(data)
        self.size += 1

    def remove_at_head(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1
        else:
            raise Exception("List is empty")

    def reverse(self):
        # a -> b -> c -> d -> None
        prev = None
        node = self.head  # a
        while node:
            temp_next = node.next  # b
            node.next = prev  # None
            prev = node  # a
            node = temp_next  # b

        self.head = prev
