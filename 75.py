class Node:
    def __init__(self,data=None,next_node=None,prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_end(self,data):
        new_node = Node(data = data,next_node = None,prev_node=self.tail)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def search_element(self,curr):
        left = self.head
        right = self.tail
        left_count = 1
        right_count = self.length
        while left is not None and right is not None and left_count <= right_count:
            if left.data == curr:
                return left_count
            elif right.data == curr:
                return right_count
            left = left.next_node
            right = right.prev_node
            left_count += 1
            right_count -= 1

list = DoublyLinkedList()

list.insert_at_end(5)
list.insert_at_end(4)
list.insert_at_end(3)
list.insert_at_end(2)
list.insert_at_end(1)
print(list.search_element(2))