class Node:
    def __init__(self,data = None,next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def get_element(self,index):
        curr = self.head
        count = 1
        while curr:
            if count == index:
                return curr.data
            curr = curr.next_node
            count += 1

    def insert_at_beginning(self,data):
        new_node = Node(data = data,next_node=self.head)
        self.head = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return False
        self.head = self.head.next_node
    
def print_list(linked_list):
    curr = linked_list.head
    while curr:
        print(curr.data,end = " ")
        curr = curr.next_node
    print()

linked_list = LinkedList()

linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(1)
print_list(linked_list)

linked_list.delete_from_beginning()
print_list(linked_list)

linked_list.insert_at_beginning(9)
print_list(linked_list)

print(linked_list.get_element(1))
print(linked_list.get_element(5))