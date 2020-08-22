class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_next(self):
        return self.next

    def __str__(self):
        pass


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

    def get_node_count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def remove_tail(self):
        if not self.tail:
            return None
        if self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            return current_tail.value
        else:
            current_tail = self.tail.value
            current_head = self.head
            while current_head.get_next() is not self.tail:
                current_head = current_head.get_next()
            self.tail = current_head
            self.tail.next = None
            return current_tail

    def new_head(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head.next
            self.head = new_node
            return new_node







