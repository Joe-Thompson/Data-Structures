"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


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

    def push(self, value):
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            return self.head.value
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            return self.head.value

    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            list_of_one = self.head.value
            self.head = None
            self.tail = None
            return list_of_one
        else:
            removed_head = self.head.value
            self.head = self.head.next
            return removed_head


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size = self.size + 1
#
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size = self.size - 1
#             return self.storage.pop(0)


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size = self.size + 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size = self.size - 1
            return self.storage.remove_head()
