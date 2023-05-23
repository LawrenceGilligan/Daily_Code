"""
Date: 05/23/2023
Time: 1h
Question: An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
Algorithm Description: The XOR linked list implementation provides a memory-efficient doubly linked list by utilizing the XOR operation to store the XOR of memory addresses instead of separate next and prev pointers.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.both = None


class XORLinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            prev_node = None
            curr_node = self.head
            next_node = None

            while curr_node is not None:
                next_node = curr_node.both ^ get_pointer(prev_node)

                if next_node is None:
                    break

                prev_node = dereference_pointer(curr_node)
                curr_node = dereference_pointer(next_node)

            new_node_address = get_pointer(new_node)
            curr_node.both = curr_node.both ^ new_node_address
            new_node.both = get_pointer(curr_node)

    def get(self, index):
        if self.head is None:
            return None

        prev_node = None
        curr_node = self.head

        for _ in range(index):
            next_node_address = curr_node.both ^ get_pointer(prev_node)
            if next_node_address is None:
                return None

            prev_node = dereference_pointer(curr_node)
            curr_node = dereference_pointer(next_node_address)

        return curr_node.value
