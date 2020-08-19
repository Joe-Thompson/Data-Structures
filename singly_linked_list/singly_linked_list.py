class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __iter__(self):
        return self


class LinkedList:
    def __init__(self):
        self.head = None  # points to first node
        self.tail = None  # points to last node

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail

    def remove_head(self):
        if not self.head:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            return current_head.value

    def remove_tail(self):
        if not self.tail:
            return None
        if self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            return current_tail.value
        else:
            current_head = self.head



