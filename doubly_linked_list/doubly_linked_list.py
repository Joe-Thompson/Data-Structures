"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value, prev=None, next=None)
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
            return new_node.value
        else:
            new_node = ListNode(value, prev=None, next=self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1
            return self.head.value

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            new_head = self.head.next
            new_head.prev = None
            current_head = self.head
            self.head = new_head
            self.length = self.length - 1
            return current_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if self.tail is None:
            new_node = ListNode(value, prev=None, next=None)
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
            return self.tail.value
        if self.tail == self.head:
            current_tail = self.tail
            new_node = ListNode(value, prev=current_tail, next=None)
            current_tail.next = new_node
            self.tail = new_node
            self.length = self.length + 1
            return self.tail.value
        else:
            current_tail = self.tail
            new_node = ListNode(value, prev=current_tail, next=None)
            current_tail.next = new_node
            self.tail = new_node
            self.length = self.length + 1
            return self.tail.value

    def move_node_to_tail(self, value):
        if self.tail is None:
            new_node = ListNode(value, prev=None, next=None)
            self.head = new_node
            self.tail = new_node
            return self.tail.value
        if self.tail == self.head:
            current_tail = self.tail
            new_node = ListNode(value, prev=current_tail, next=None)
            current_tail.next = new_node
            self.tail = new_node
            return self.tail.value
        else:
            current_tail = self.tail
            new_node = ListNode(value, prev=current_tail, next=None)
            current_tail.next = new_node
            self.tail = new_node
            return self.tail.value

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return None
        if self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        else:
            current_tail = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.length = self.length - 1
            return current_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        new_head = node
        current_head = self.head
        current_head.prev = new_head
        new_head.next = current_head
        self.head = new_head

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        node_value = node.value
        self.delete(node)
        self.add_to_tail(node_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node == node:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                current_node = current_node.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.value
        else:
            current_max = self.head.value
            current_node = self.head
            while current_node is not None:
                if current_max < current_node.value:
                    current_max = current_node.value
            current_node = current_node.next
        return current_max
